from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from django.utils import timezone
from .models import Post

from .forms import InputForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




# def home(request):
#     response = requests.get('http://api.ipstack.com/73.49.208.176?access_key=e9b82d71414370801e72f9b412c7c283')
#     geodata = response.json()
#     return render(request, 'blog/home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     })


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://api.ipstack.com/73.49.208.176?access_key=e9b82d71414370801e72f9b412c7c283')
    geodata = response.json()
    return render(request, 'blog/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyCV6c_Aj4-0BdIBmV2M1CCCkGYqWA_aUFk'  # Don't do this! This is just an example. Secure your keys properly.
    })


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            #get form information into variables for API call
            data = request.POST.copy()
            airline = data.get('airline')
            flight_number = data.get('flight_number')
            year = data.get('date_year')
            month = data.get('date_month')
            day = data.get('date_day')

            # API call to get basic flight information
            api_request = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{}/{}/dep/{}/{}/{}?" \
                          "appId=b3f88651&appKey=76d0bca1d9792a4398dd99018d957d3e&utc=false".format(airline,flight_number,year, month,day)
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            response = requests.get(api_request)
            flightstatus = response.json()
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            departure_airport = flightstatus['flightStatuses'][0]['departureAirportFsCode']
            arrival_airport =   flightstatus['flightStatuses'][0]['arrivalAirportFsCode']
            departure_staus = flightstatus['flightStatuses'][0]['status']

            #API call to get depature airport weather
            api_request_wx_dep = "https://api.flightstats.com/flex/weather/rest/v1/json/all/{}?appId=b3f88651&appKey=76d0bca1d9792a4398dd99018d957d3e".format(departure_airport)
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            response = requests.get(api_request_wx_dep)
            departure_wx = response.json()
            departure_instrumentation_condition = departure_wx['metar']['tags'][0]['value']
            deprature_prevailing_condition = departure_wx['metar']['tags'][1]['value']

            #Calculate a departure "score" based on flight status  "S" stands for scheduled, all others are flight delayed
            if departure_staus == "S":
                departure_score = 15
            else:
                departure_score = 50

            #Add to departure score based on the weather at the departure airport Instrumnetation conditions
            if departure_instrumentation_condition == ("IFR"):
                departure_score += 15
            else:
                departure_score += 5

            #Add to departure score based on the weather at the departure airport prevailing conditions
            if departure_instrumentation_condition == ("Hurricane" or "Tornado" or "Volcanic Ash"):
                departure_score += 50
            elif departure_instrumentation_condition == ("Ice" or "Thunderstorms" or "Snow" or "Fog" or "Smoke"):
                departure_score += 30
            elif departure_instrumentation_condition == ("Patchy Fog" or "Windy" or "Breezy" or "Rain" or "Showers"):
                departure_score += 10
            else:
                departure_score += 0




            #API call to get arrival airport weather
            api_request_wx_arr = "https://api.flightstats.com/flex/weather/rest/v1/json/all/{}?appId=b3f88651&appKey=76d0bca1d9792a4398dd99018d957d3e".format(arrival_airport)
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            response = requests.get(api_request_wx_arr)
            arrival_wx = response.json()
            arrival_instrumentation_condition = departure_wx['metar']['tags'][0]['value']
            arrival_prevailing_condition = departure_wx['metar']['tags'][1]['value']

            #Add to departure score based on the weather at the departure airport Instrumnetation conditions
            if arrival_instrumentation_condition == ("IFR"):
                arrival_score += 15
            else:
                arrival_score += 5

            #Add to departure score based on the weather at the departure airport prevailing conditions
            if departure_instrumentation_condition == ("Hurricane" or "Tornado" or "Volcanic Ash"):
                arrival_score += 50
            elif departure_instrumentation_condition == ("Ice" or "Thunderstorms" or "Snow" or "Fog" or "Smoke"):
                arrival_score += 30
            elif departure_instrumentation_condition == ("Patchy Fog" or "Windy" or "Breezy" or "Rain" or "Showers"):
                arrival_score += 10
            else:
                arrival_score += 0












            return render(request, 'fdp/predict.html', {
            'flightId': flightstatus['flightStatuses'][0]['flightId'],
            'departureAirport': flightstatus['flightStatuses'][0]['departureAirportFsCode'],
            'arrivalAirport': flightstatus['flightStatuses'][0]['arrivalAirportFsCode'],
            'flightNumber': flightstatus['flightStatuses'][0]['flightNumber'],



                #'api_key': 'AIzaSyCV6c_Aj4-0BdIBmV2M1CCCkGYqWA_aUFk'  # Don't do this! This is just an example. Secure your keys properly.
    })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'fdp/index.html', {'form': form})









def get_travelr(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/predict/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'travelr-master/index.html', {'form': form})
