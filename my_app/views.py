import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get('https://losangeles.craigslist.org/search/bbb?query=python%20tutor&sort=rel')
    data = response.text
    print(data)

    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
