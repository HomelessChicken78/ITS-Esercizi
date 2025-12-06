import requests
import json

url : str = "http://127.0.0.1:5000/"
headers : dict[str, str] = {
    "Content-Type" : "Application/json",
    "Accept" : "Application/json"
}

print("\nGET /")
response = requests.get(
    url=url,
    headers=headers
)
print(json.dumps(response.json(), indent=4))



print("\nGET /devices")
response = requests.get(
    url=url + "devices",
    headers=headers
)
print(json.dumps(response.json(), indent=4))



print("\nGET /devices/d1")
response = requests.get(
    url=url + "devices/d1",
    headers=headers
)
print(json.dumps(response.json(), indent=4))



print("\nGET /devices/non_esisto")
response = requests.get(
    url=url + "devices/non_esisto",
    headers=headers
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nGET /devices/d1/estimate/1.5")
response = requests.get(
    url=url + "devices/d1/estimate/1.5",
    headers=headers
)
print(json.dumps(response.json(), indent=4))



print("\nPOST /devices (missing fields)")
response = requests.post(
    url=url + "devices",
    headers=headers,
    json={
        "device_type" : "smartphone",
        "model" : "Google Pixel 8",
        "customer_name" : "Ferdinando Mortadellini",
        "status" : "received"
    }
)
print(json.dumps(response.json(), indent=4)  + ", " + str(response.status_code))



print("\nPOST /devices (wrong value for field)")
response = requests.post(
    url=url + "devices",
    headers=headers,
    json={
        "device_type" : "smartphone",
        "model" : "Google Pixel 8",
        "customer_name" : "Ferdinando Mortadellini",
        "status" : "completato al 100%",
        "purchase_year" : 2022,
        "storage_gb" : 128
    }
)
print(json.dumps(response.json(), indent=4)  + ", " + str(response.status_code))



print("\nPOST /devices (phone)")
response = requests.post(
    url=url + "devices",
    headers=headers,
    json={
        "device_type" : "smartphone",
        "model" : "Google Pixel 8",
        "customer_name" : "Ferdinando Mortadellini",
        "status" : "received",
        "purchase_year" : 2022,
        "storage_gb" : 128
    }
)
print(json.dumps(response.json(), indent=4)  + ", " + str(response.status_code))



print("\nPOST /devices (laptop)")
response = requests.post(
    url=url + "devices",
    headers=headers,
    json={
        "device_type" : "laptop",
        "model" : "MacBook Air",
        "customer_name" : "David Divano",
        "status" : "received",
        "purchase_year" : 2020,
        "screen_size_inches" : 15.6,
        "has_dedicated_gpu" : False
    }
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nPOST /devices (d4)")
requests.post(
    url=url + "devices",
    headers=headers,
    json={
        "device_type" : "laptop",
        "model" : "Sedia da gaming",
        "customer_name" : "Mario Mela",
        "status" : "received",
        "purchase_year" : 2019,
        "screen_size_inches" : 12.6,
    }
)
print("DELETE /devices/d4 (successful)")
response = requests.delete(
    url=url + "devices/d4",
    headers=headers
)
print("GET /devices/d4")
response = requests.get(
    url=url + "devices/d4",
    headers=headers
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nDELETE /devices/d4 (unsuccessful)")
response = requests.delete(
    url=url + "devices/d400",
    headers=headers
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nPUT /devices/d3 (succesful)")
response = requests.put(
    url=url + "devices/d3",
    headers=headers,
    json={
    "device_type" : "smartphone",
    "model" : "Xiami 14",
    "customer_name" : "David Divano",
    "status" : "ready",
    "purchase_year" : 2022,
    "storage_gb" : 128,
    "has_protective_case" : False
}
)
print("GET /devices/d3")
response = requests.get(
    url=url + "devices/d3",
    headers=headers
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nPUT /devices/d6 (unsuccesful)")
response = requests.put(
    url=url + "devices/d7",
    headers=headers,
    json={
    "device_type" : "laptop",
    "model" : "Lenovo",
    "customer_name" : "Gainfrancesco De Libertini",
    "status" : "ready",
    "purchase_year" : 2023,
    "screen_size_inches" : 12.6,
}
)
print("GET /devices/d6")
response = requests.get(
    url=url + "devices/d6",
    headers=headers
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))



print("\nPATCH /devices/d0")
response = requests.patch(
    url=url + "devices/d0", 
    headers=headers, 
    json={
    "status": "repairing"
}
)
print(json.dumps(response.json(), indent=4) + ", " + str(response.status_code))