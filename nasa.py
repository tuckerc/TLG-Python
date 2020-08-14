#!/usr/bin/env python3
import requests

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = f'start_date={input("pick a start date (yyyy-mm-dd): ")}'
enddate = f'&end_date={input("pick an end date (yyyy-mm-dd): ")}'
mykey = '&api_key=g70uKEwpPJQVB4Vo7K4S7AlOITT86VfGPZG3t3BZ'

neourl = neourl + startdate + mykey

## Call the webservice
neos = dict((requests.get(neourl)).json())['near_earth_objects']
print(f"\n!!!!!! POTENTIALLY HAZARDOUS ASTEROIDS !!!!!!")
for key, val in neos.items():
    for i in range(len(val)):
        if val[i]['is_potentially_hazardous_asteroid']:
            link = val[i]['nasa_jpl_url']
            print(link)
