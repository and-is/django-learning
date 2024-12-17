import requests

# endpoint = "https://httpbin.org/anything"
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"product_id": 123 })   # HTTP Request

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# print(get_response.headers)

print(get_response.json())