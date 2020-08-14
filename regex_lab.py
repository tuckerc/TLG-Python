#!/usr/bin/ python3
import urllib.request
import re
import pprint

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

match = re.findall(searchFor, searchMe)

if match:
    pprint.pprint(f"Found {len(match)} matches")
else:
    print("No match!")
