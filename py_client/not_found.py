import requests

endpoint = "http://localhost:8000/api/products/99999999999999999"

get_response = requests.get(endpoint)

print(get_response.text)