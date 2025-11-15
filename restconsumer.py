import requests # install this library from the command line: 
# $ python -m pip install requests
import json

BASE_URL = "http://localhost:5088/api/aktiehandel"

response = requests.get(BASE_URL)
print(f"GET status code {response.status_code}")
print(response.json())

AKTIE_DICTIONARY = {
    "navn": "Mit selskab",
    "antal": 45,
    "pris": 11
}
data_json = json.dumps(AKTIE_DICTIONARY)
HEADERS = {"Content-Type": "application/json"}
# TODO ... json = ... ej med PUT
response = requests.post(BASE_URL, data=data_json, headers=HEADERS)

print(f"POST status code {response.status_code}")
print(response.json())  

response = requests.delete(BASE_URL + "/1")
print(f"DELETE status code {response.status_code}")
if response.status_code == 200:
    print(response.json())

response= requests.put(BASE_URL + "/2", data=data_json, headers=HEADERS)
print(f"PUT status code {response.status_code}")
print(response.json())