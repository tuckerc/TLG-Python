#!/usr/bin/python3
import requests
import wget


def api_pull():
    choice = ""
    while choice == "":
        choice = input("What Pokemon would you like a picture of? ")
    return 'https://pokeapi.co/api/v2/pokemon/' + choice.strip().lower()


def json_conv(poke_api):
    """function that takes the URL from player 1 and converts it from JSON to Python"""
    r = requests.get(poke_api)
    return r.json()


def api_slice(json2python):
    poke_pic = json2python.get("sprites").get("front_default")
    return poke_pic


def wget_pic(imagelink):
    wget.download(imagelink, "/home/student/mycode/pokemon.png")


def main():
    wget_pic(api_slice(json_conv(api_pull())))


main()
