import requests

API="http://api.openweathermap.org/data/2.5/weather?q=Modena,it&appid=&lang=it"
response=requests.get(API).json()
description=response["weather"][0]["description"]
temp=float(response["main"]["temp"])
temp=round(temp-273.15,2)
temp_min=float(response["main"]["temp_min"])
temp_min=round(temp_min-273.15,2)
temp_max=float(response["main"]["temp_max"])
temp_max=round(temp_max-273.15,2)
