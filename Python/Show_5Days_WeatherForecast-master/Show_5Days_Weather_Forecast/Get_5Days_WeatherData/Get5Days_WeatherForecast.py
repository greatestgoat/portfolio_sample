"""
    version:1.1

"""
import json
import datetime
import os
import requests
import sys

from pytz import timezone
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

API_KEY = 'YourAPIKeys'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
API_URL = BASE_URL + '?id={id}&APPID={key}'

def getWeatherForecast(ID):
    
    url = API_URL.format(id=ID, key=API_KEY)
    response = requests.get(url)
    forecastData = json.loads(response.text)
    
    if not ('list' in forecastData):
        print('error')
        return

    forecastDatetime = []
    weatherDescription = []
    temperature = []
    rainfall = []

    for item in forecastData['list']:
        forecastDatetime.append(timezone(
            'UTC').localize(datetime.datetime.fromtimestamp(item['dt'])))
        weatherDescription.append(item['weather'][0]['description'])
        temperature_temp = item['main']['temp']
        temperature.append(Decimal(temperature_temp-275.15)
                .quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        # rainfall = 0
        if 'rain' in item and '3h' in item['rain']:
            rainfall.append(item['rain']['3h'])
            rain = item['rain']['3h']
        else:
            rainfall.append(0)
        #     rain = ''
        # print('Time(UTC):{0} Weather:{1} Temperature(℃):{2} Rainfall(mm):{3}'.format(
        #     datetime.datetime.fromtimestamp(item['dt']), item['weather'][0]['description'], Decimal(temperature_temp-275.15).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), rain))
    return forecastDatetime, weatherDescription, temperature, rainfall
#     print('Time(UTC):{0} Weather:{1} Temperature(℃):{2} Rainfall(mm):{3}'.format(
#             forecastDatetime, weatherDescription, temperature, rainfall))

# getWeatherForecast(1861060)
