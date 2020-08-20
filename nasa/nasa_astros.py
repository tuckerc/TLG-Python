#!/usr/bin/env python3
import requests

# build url
url = 'http://api.open-notify.org/astros.json'

# Call nasa api
astros = dict((requests.get(url)).json())
print(f"People in space: {astros.get('number')}")
for person in astros.get('people'):
    print(f"{person.get('name')} on the {person.get('craft')}")
