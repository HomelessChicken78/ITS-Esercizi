import requests, json

URL: str = "http://127.0.0.1:5000/"
headers : dict[str, str] = {
        "Content-Type" : "Application/json",
        "Accept" : "Application/json"
    }

print("\nGET /")
response = requests.get(
    url=URL,
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /vehicles")
response = requests.get(
    url=URL+"/vehicles",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /vehicles/ABC123")
response = requests.get(
    url=URL+"/vehicles/ABC123",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /vehicles/ABC123/prep-time/1.0")
response = requests.get(
    url=URL+"/vehicles/ABC123/prep-time/1.0",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /vehicles - Wrong payload")
response = requests.post(
    url=URL + "/vehicles",
    headers=headers,
    data={
    "model": "Sedan",
    "vehicle_type": "car",
    "registration_year": 2020,
    "status": "available"
}
)
print(response.status_code)

print("\nPOST /vehicles - Car")
response = requests.post(
    url=URL + "/vehicles",
    headers=headers,
    json={
    "plate_id": "PPP000",
    "model": "Sedan",
    "vehicle_type": "car",
    "registration_year": 2020,
    "status": "available",
    "doors": 4,
    "is_cabrio": False
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /vehicles - Van")
response = requests.post(
    url=URL + "/vehicles",
    headers=headers,
    json={
    "plate_id": "NNN233",
    "model": "Van Model X",
    "vehicle_type": "van",
    "registration_year": 2018,
    "status": "Retired",
    "max_load_kg": 1500,
    "require_special_license": True
}
)
print(json.dumps(response.json(), indent=4))

print("\nPUT /vehicles/ABC123 - Già esiste")
response = requests.put(
    url=URL + "/vehicles/ABC123",
    headers=headers,
    json={
    "plate_id": "runydfeui",
    "model": "Qualcosa",
    "vehicle_type": "car",
    "registration_year": 2025,
    "status": "available",
    "doors": 2,
    "is_cabrio": True
}
)
print(json.dumps(response.json(), indent=4))

print("\nPUT /vehicles/ABC123 - Non esiste")
response = requests.put(
    url=URL + "/vehicles/fehiou",
    headers=headers,
    json={
    "plate_id": "fehiou",
    "model": "Marco",
    "vehicle_type": "car",
    "registration_year": 2022,
    "status": "available",
    "doors": 5,
    "is_cabrio": False
}
)
print(json.dumps(response.json(), indent=4))
