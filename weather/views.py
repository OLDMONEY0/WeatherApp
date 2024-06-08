from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '94d3fcc1ab0987b085725122cf371220'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid



    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()




    city = 'Almaty'
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(info)

    context = {'all_info': all_cities, 'form': form}


    return render(request, 'index.html', context) 
