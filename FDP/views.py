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

            data = request.POST.copy()
            airline = data.get('airline')
            flight_number = data.get('flight_number')


            api_request = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{}/{}/dep/2019/05/11?appId=b3f88651&appKey=76d0bca1d9792a4398dd99018d957d3e&utc=false".format(airline,flight_number)
            print(api_request)
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            response = requests.get(api_request)
            flightstatus = response.json()
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
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

    return render(request, 'fdp/name.html', {'form': form})









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
