from django.shortcuts import render
import requests
from django.utils import timezone
from .models import Post

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
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://api.ipstack.com/73.49.208.176?access_key=e9b82d71414370801e72f9b412c7c283')
    geodata = response.json()
    return render(request, 'fdp/index.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyCV6c_Aj4-0BdIBmV2M1CCCkGYqWA_aUFk'  # Don't do this! This is just an example. Secure your keys properly.
    })
