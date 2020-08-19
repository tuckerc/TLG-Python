#!/usr/bin/env python3
import requests
from pprint import pprint
from wget import download
from os import environ

# build url
url = 'https://api.nasa.gov/planetary/apod?'
date = f'date={input("pick a date after 1995-06-16 (yyyy-mm-dd): ")}'
mykey = f'&api_key={environ.get("API_KEY")}'
apodurl = url + date + mykey

# Call nasa api
apod = dict((requests.get(apodurl)).json())
pic_data = {'date': apod.get('date'), 'title': apod.get('title'), 'description': apod.get('explanation')}
pprint(f"\nPicture of the day:\n{pic_data}")
download(apod.get('url'))
