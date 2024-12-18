import requests

endpoint = "http://localhost:8000/api/products/"

data={
    "title":"Done done done",
    "price": 11.99
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())