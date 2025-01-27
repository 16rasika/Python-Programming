import api
import requests
#import os
#from datetime import datetime

user_input = input('Enter city: ')
#print(user_input)

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api.api_key}")

if weather_data .json()['cod'] == '404':
   print("No city found")

else:
   weather = weather_data.json()['weather'][0]['main']
   temp = round(weather_data.json()['main']['temp'])


   print (f"The weather in {user_input} is: {weather}")
   print(f"The temperature in {user_input} id {temp} ºF")

