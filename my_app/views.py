import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    response = requests.get('https://losangeles.craigslist.org/search/bbb?query=python%20tutor&sort=rel')
    data = response.txt
    print(data)

    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
