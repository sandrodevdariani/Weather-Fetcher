import requests

API_key = '7e657a2c300e3d7aedd733169a025b31'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city_name = input('enter city name: ')
request_url = f"{BASE_URL}?q={city_name}&appid={API_key}"
respone = requests.get(request_url)

if respone.status_code == 200:
    data = respone.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    temp_celsius = temperature - 273.15
    print('weather:', weather)
    print('temp:', temp_celsius , 'Celsius')
else:
    print('an error occured')



