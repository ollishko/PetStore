import requests

url = "https://petstore.swagger.io/v2/store/order/8"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
