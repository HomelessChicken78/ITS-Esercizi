# Avviare prima rifugio_animali/main
import requests, json

if __name__ == "__main__":
    headers = {
        'Content-type' : 'application/json',
        'Accept' : 'application/json'
    }

    print("list animals")
    response = requests.get(
        url = "http://127.0.0.1:5000/animals",
        headers=headers
    )
    print(response.json())

    print("\nget animal with id c1")
    response = requests.get(
        url = "http://127.0.0.1:5000/animals/c1",
        headers=headers
    )
    print(response.json())

    print("\npost new animal")
    payload = {
        "species" : "dog",
        "name" : "Coconut",
        "age_years" : 2,
        "weight_kg" : 22,
        "breed" : "dalmatain",
        "is_trained" : False
    }
    response = requests.post(
       url = "http://127.0.0.1:5000/animals",
       json=payload,
       headers=headers 
    )
    print(response.json())

    print("\nadd adoption for animal")
    payload = {
        "adopter_name" : "Maria Gianfranceschini"
    }
    response = requests.post(
       url = "http://127.0.0.1:5000/animals/d3/adoption",
       json=payload,
       headers=headers 
    )
    print(response.json())

    print("\nget adoption")
    response = requests.get(
        url=f"http://127.0.0.1:5000{response.json()['_links']['get adoption']['endpoint']}",
        headers=headers
    )
    print(response.json())

    print("\nget food")
    response = requests.get(
        url="http://127.0.0.1:5000/animals/d3/food",
        headers=headers
    )
    print(response.json()) 
