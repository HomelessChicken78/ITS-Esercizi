import requests
import json

URL = "http://127.0.0.1:5000/"
headers = {
    "Content-type" : "application/json",
    "Accept" : "application/json"
}

print("GET /")
response = requests.get(
    url = URL,
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /devices")
response = requests.get(
    url = URL + "devices",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /devices/iurh - does not exist")
response = requests.get(
    url = URL + "devices/iurh",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /devices/CAM001 - exists")
response = requests.get(
    url = URL + "devices/CAM001",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nGET /devices/CAM001/diagnostic/1.0")
response = requests.get(
    url = URL + "devices/CAM001/diagnostic/1.0",
    headers=headers
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /devices - succesful")
response = requests.post(
    url = URL + "devices",
    headers=headers,
    json={
        "serial_number" : "BULB0994",
        "brand" : "Coccodrillo",
        "room" : "Entrance",
        "installation_year" : 2023,
        "status" : "updating",
        "type" : "smartbulb",
        "brightness_lumens" : 600,
        "color_capability" : False
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /devices (unsuccesful - already exists")
response = requests.post(
    url = URL + "devices",
    headers=headers,
    json={
        "serial_number" : "BULB0994",
        "brand" : "Coccodrillo",
        "room" : "Entrance",
        "installation_year" : 2023,
        "status" : "updating",
        "type" : "smartbulb",
        "brightness_lumens" : 600,
        "color_capability" : False
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /devices (unsuccesful - missing field")
response = requests.post(
    url = URL + "devices",
    headers=headers,
    json={
        "serial_number" : "ffed8y",
        "brand" : "Mortadella",
        "room" : "Kitchen",
        "status" : "updating",
        "type" : "smartbulb",
        "brightness_lumens" : 600,
        "color_capability" : False
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPOST /devices (unsuccesful - invalid value for status")
response = requests.post(
    url = URL + "devices",
    headers=headers,
    json={
        "serial_number" : "Bright944",
        "brand" : "BrightElectro",
        "room" : "Bedroom",
        "status" : "idk",
        "type" : "smartbulb",
        "installation_year" : 2026,
        "brightness_lumens" : 750,
        "color_capability" : True
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPUT /devices/ABC123 - new device")
response = requests.put(
    url = URL + "devices/ABC123",
    headers=headers,
    json={
        "serial_number" : "CAM231",
        "brand" : "EyesOfFalcon",
        "room" : "Entrance",
        "status" : "online",
        "type" : "camera",
        "installation_year" : 2022,
        "resolution" : "1048p",
        "night_vision" : False
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPUT /devices/CAM231 - already exists")
response = requests.put(
    url = URL + "devices/CAM231",
    headers=headers,
    json={
        "serial_number" : "CAM FAL12-234",
        "brand" : "Falcon12",
        "room" : "Entrance",
        "status" : "offline",
        "type" : "camera",
        "installation_year" : 2023,
        "resolution" : "720p",
        "night_vision" : True
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPATCH /devices/BULB001 - exists")
response = requests.patch(
    url = URL + "devices/BULB001",
    headers=headers,
    json={
        "status" : "error"
    }
)
print(json.dumps(response.json(), indent=4))

print("\nPATCH /devices/FO009 - does not exist")
response = requests.patch(
    url = URL + "devices/FO009",
    headers=headers,
    json={
        "status" : "updating"
    }
)
print(json.dumps(response.json(), indent=4))

print("\nDELETE /devices/BULB002 - exists")
response = requests.delete(
    url = URL + "devices/BULB002",
    headers=headers,
)
print("Eliminazione riuscita" if response.status_code == 204 else json.dumps(response.json(), indent=4))

print("\nDELETE /devices/FO009 - does not exist")
response = requests.delete(
    url = URL + "devices/FO009",
    headers=headers,
)
print("Eliminazione riuscita" if response.status_code == 204 else json.dumps(response.json(), indent=4))