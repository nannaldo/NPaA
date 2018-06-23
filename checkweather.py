#!/usr/bin/python
__author__ = 'Giovanni Pelliccia'

#checkweather.py: Get weather data from .
#use at your own risk

#import
import requests

openweatherapi="http://api.openweathermap.org/data/2.5/weather?APPID=8e82d50e24d5982aa346eadbd96c2bc6&id=3175058&id=6539761"
output=requests.get(openweatherapi)
jsonOutput=output.json()
print jsonOutput['name']
print jsonOutput['main']['temp']


