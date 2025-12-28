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
    json={
    "model": "Sedan",
    "vehicle_type": "car",
    "registration_year": 2020,
    "status": "available"
}
)
print(response.status_code, " " + json.dumps(response.json()))

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

print("\nPOST /vehicles - already exists")
response = requests.post(
    url=URL + "/vehicles",
    headers=headers,
    json={
    "plate_id": "ABC123",
    "model": "Van Model X",
    "vehicle_type": "van",
    "registration_year": 2018,
    "status": "Retired",
    "max_load_kg": 1500,
    "require_special_license": True
}
)
print(json.dumps(response.json(), indent=4))

print("\nPUT /vehicles/ABC123 - already exists")
response = requests.put(
    url=URL + "/vehicles/ABC123",
    headers=headers,
    json={
    "plate_id": "ABC123",
    "model": "Qualcosa",
    "vehicle_type": "car",
    "registration_year": 2025,
    "status": "available",
    "doors": 2,
    "is_cabrio": True
}
)
print(json.dumps(response.json(), indent=4)) #ABC123 removed. Added runydfeui

print("\nPUT /vehicles/fehiou - does not exist")
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

print("\nPATCH /vehicles/NNN233/status - exists")
response = requests.patch(
    url=URL + "/vehicles/NNN233/status",
    headers=headers,
    json={
        "status" : "reNTed"
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPATCH /vehicles/iuybe/status - does not exists")
response = requests.patch(
    url=URL + "/vehicles/iuybe/status",
    headers=headers,
    json={
        "status" : "Maintenance"
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPATCH /vehicles/NNN233/status - status invalid")
response = requests.patch(
    url=URL + "/vehicles/NNN233/status",
    headers=headers,
    json={
        "status" : "Cocco bello"
    }
)
print(json.dumps(response.json(), indent=4))

print("\nDELETE /vehicles/PPP000 - exists")
response = requests.delete(
    url=URL + "/vehicles/PPP000",
    headers=headers,
)
print(json.dumps(response.json(), indent=4))

print("\nDELETE /vehicles/uhidi - does not exists")
response = requests.delete(
    url=URL + "/vehicles/uhidi",
    headers=headers,
)
print(json.dumps(response.json(), indent=4))