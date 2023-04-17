import requests

ciudad = input("Dime una Ciudad: ")
params = {
  'access_key': '3814acbde3108b3c251e2654e9573de5',
  'query': ciudad
}

api_result = requests.get('http://api.weatherstack.com/current', params)

data = api_result.json()
location = data['location']['name']
temperature = data['current']['temperature']
description = data['current']['weather_descriptions'][0]
print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius.')

