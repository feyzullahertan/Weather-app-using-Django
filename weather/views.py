#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Feyzullah ERTAN
# @updatedDate: 05.05.2020
# @version: 1.0.2


import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def toCelsius(tmp):
    celcius = (tmp - 32) * 5.0/9.0
    return celcius

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&lang=tr&appid=YOUR_API_KEY'
    hata_msj = ''
    mesaj = ''
    mesaj_sinif = ''
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            yeni_sehir = form.cleaned_data['name']
            r = requests.get(url.format(yeni_sehir)).json()
            girilen_sehir = r['name']  # şehir adı girilen yer
            mevcut_sehir_sayisi = City.objects.filter(name=girilen_sehir).count()
            if mevcut_sehir_sayisi  == 0:
                if r['cod'] == 200:
                    City.objects.create(name=girilen_sehir)
                else:
                    hata_msj = 'API Servisinde böyle bir şehir yok!'
            else:
                hata_msj = 'API Servisinde böyle bir şehir yok!'
        if hata_msj:
            mesaj = hata_msj
            mesaj_sinif = 'is-danger'
        else:
            mesaj = 'Şehir eklendi'
            mesaj_sinif = 'is-success'

    form = CityForm()
    cities = City.objects.all()

    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()
        cels=toCelsius(round(r['main']['temp'],1))
        city_weather = {
            'city' : city.name,
            'temperature' : cels,
            'description' : r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'coordinatesX': r['coord']['lon'],
            'coordinatesY': r['coord']['lat']
        }
        #city_weather.temperature=toCelcius(round(city_weather.temperature,1)
        weather_data.append(city_weather)
    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : mesaj,
        'message_class' : mesaj_sinif
    }
    
    return render(request, 'weather/index.html' , context)
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
