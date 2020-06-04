import requests
import itertools
a=["model2010","model2015","model2020"]
b=["km0","km50000","km100000"]
c=["hp80","hp160","hp240"]
e=["tork100","tork200","tork300"]
d= []
c = list(itertools.product(a, b,c,e))
for i in c:
    if i[0] not in i[1]:
        d.append(i)
for i in d:
    print(i)




"""
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=793dc9b3649fba1d42682e70e74d413d'
city="Las Vegas"
r=requests.get(url.format(city)).json()
weather_data=[]
city_weather = {
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'coordinatesX': r['coord']['lon'],
            'coordinatesY': r['coord']['lat']
        }
#city_weather.temperature=toCelcius(round(city_weather.temperature,1)
weather_data.append(city_weather)
print(weather_data[0])
print(list(weather_data[0].values())[0])
"""
"""
def toCelsius(tmp):
    celcius = (tmp - 32) * 5.0/9.0
    return celcius

print(round(toCelsius(80),1))"""
