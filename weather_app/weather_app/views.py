from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    if request.method == "GET":
        city = request.GET.get('city_name')
        if not city:
            pass
            # # Handle the case when the city is not provided in the request
            # return HttpResponse("Please provide a city name")
        api_key = "0b9ee64e1ed48235987ecc54ff179212"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url).json()
        data = {
           'temperature': round(float(response['main']['temp'] - 273),3),
           'description': response['weather'][0]['description'],
           'pressure': round(float((response['main']['pressure'])/100),3),
           'wind': response['wind']['speed'],
           'humidity': response['main']['humidity'],
           'icon':response['weather'][0]['icon'],
           'name':response['name']
        }
        #print(data)
        content={'data':data}
        return render(request, "index.html", content)
