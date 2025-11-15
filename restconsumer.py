import requests # install this library from the command line: 
# $ python -m pip install requests

BASE_URL = "http://localhost:5088/api/aktiehandel"

response = requests.get(BASE_URL)
print(f"GET status code {response.status_code}")
if response.status_code == 200:
  print(response.json())

AKTIE_DICTIONARY = {
    "navn": "Mit selskab",
    "antal": 45,
    "pris": 11
}

response = requests.post(BASE_URL, json=AKTIE_DICTIONARY)
# json= automatically converts the dictionary to a JSON string
# json= automatically sets the Content-Type header to application/json
 
print(f"POST status code {response.status_code}")
if response.status_code == 201:
  print(response.json())  

url = BASE_URL + "/1"
response = requests.delete(url)
print(f"DELETE status code {response.status_code}")
if response.status_code == 200:
    print(response.json())

url = f"{BASE_URL}/2"
response= requests.put(url, json=AKTIE_DICTIONARY)
print(f"PUT status code {response.status_code}")
if response.status_code == 200:
  print(response.json())