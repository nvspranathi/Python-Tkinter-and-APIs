import json
import requests

# API - to fetch temperature of a city

city_name = input('Enter a City Name: ')
print(city_name)
api_key = '104319008bec789609e661e74a3536c9'

# To build the API URL
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_info = requests.get(api_url)
data = get_server_info.json()
# print(data)
# for pretty formatting the json data
pretty_data = json.dumps(data,indent=4)
print(pretty_data)
# to fetch specific data from Json
D = data["weather"][0]['description']
main_data = data['main']
print(D, main_data)