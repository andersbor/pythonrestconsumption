import requests # install this library: $ python -m pip install requests
import json

response = requests.get("http://localhost:5088/api/aktiehandel")
print(response.status_code)
print(response.json())

data = {
    "navn": "Mit selskab",
    "antal": 45,
    "pris": 11
}
data = json.dumps(data)
headers = {"Content-Type": "application/json"}
response = requests.post("http://localhost:5088/api/aktiehandel/", data=data, headers=headers)

print(response.status_code)
print(response.json())  

response = requests.delete("http://localhost:5088/api/aktiehandel/1")
print(response.status_code)
if response.status_code == 200:
    print(response.json())

response= requests.put("http://localhost:5088/api/aktiehandel/2", data=data, headers=headers)
print(response.status_code)
print(response.json())