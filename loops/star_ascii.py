#!/usr/bin/env python3


import sys

number_of_stars = sys.argv[1]

stars = ""
star_range = range(int(number_of_stars))
for i in star_range:
    stars = stars + "*"
    print(stars)
for i in star_range:
    stars = stars[0:-1]
    print(stars)
