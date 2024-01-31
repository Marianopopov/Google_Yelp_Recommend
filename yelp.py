import requests
from decouple import config

API_KEY = config('YELP_API_KEY')

url = "https://api.yelp.com/v3/businesses/search"


url = "https://api.yelp.com/v3/businesses"



headers = {
    "Authorization": f"Bearer {API_KEY}",
}

params = {
    "term": "Food Truck",
    "location": "San Francisco",
}

params = {
    "id" : '3uLgwr0qeCNMjKenHJwPGQ',
    "location": "San Francisco",
}

response = requests.get(url, headers=headers, params=params)

print(response)

data = response.json()

# Maneja los datos obtenidos según tus necesidades
print(data['businesses'])

