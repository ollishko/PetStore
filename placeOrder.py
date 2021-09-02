import requests
import json

url = "https://petstore.swagger.io/v2/store/order"

payload = json.dumps({
  "id": 8,
  "petId": 125,
  "quantity": 5,
  "shipDate": "2021-09-02T11:05:04.251Z",
  "status": "placed",
  "complete": True
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)