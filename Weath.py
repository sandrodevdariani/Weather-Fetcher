import requests

API_KEY = '7e657a2c300e3d7aedd733169a025b31'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('enter city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
respone = requests.get(request_url)

if respone.status_code == 200:
    data = respone.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print('weather:', weather)
    print('temp:', temperature, 'Farnh')
else:
    print('an error occured')
