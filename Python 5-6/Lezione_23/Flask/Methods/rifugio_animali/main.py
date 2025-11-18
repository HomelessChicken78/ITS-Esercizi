from abc import ABC, abstractmethod
from typing import Self

class Animal(ABC):
    '''La classe Animal rappresenta un animale generico del rifugio.'''

    ids: dict[int, Self] = dict()

    def __init__(self, name : str, age_years : int, weight_kg : float):
        if Animal.ids:
            max_id = max(int(k[1:]) for k in Animal.ids.keys())

        else:
            max_id = 0
        
        match self.species():
            case "dog":
                self.id = f'd{max_id + 1}'
            case "cat":
                self.id = f'c{max_id + 1}'
            case _:
                self.id = f'a{max_id + 1}'

        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

        Animal.ids[self.id] = self

    @abstractmethod    
    def species(self) -> str:
        '''Restituire la specie dell’animale, ad esempio "dog" o "cat".'''
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        '''Restituire la quantità di cibo giornaliera raccomandata in grammi.'''
        pass

    def info(self) -> dict[str, str|int|float]:
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg,
            }
    
    def bmi_like(self) -> float:
        '''Restituisce un valore derivato (simile a un indice di “forma fisica”)'''
        return self.weight_kg / (self.age_years + 1)


class Dog(Animal):
    '''La classe Dog rappresenta un cane'''
    def __init__(self, name : str, age_years : int, weight_kg : float, breed : str, is_trained : bool = False):
        super().__init__(name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained
    
    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> int:
        return 200 + self.age_years * 500
    
    def info(self) -> dict[str, str|int|float|bool]:
        base = super().info()
        base["breed"] = self.breed
        base["is_trained"] = self.is_trained
        return base


class Cat(Animal):
    '''La classe Cat rappresenta un gatto'''
    def __init__(self, name : str, age_years : int, weight_kg : float, favourite_toy : str, indoor_only : bool = False):
        super().__init__(name, age_years, weight_kg)
        self.favourite_toy = favourite_toy
        self.indoor_only = indoor_only

    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self) -> int:
        return 100 + self.age_years * 30

    def info(self) -> dict[str, str|int|float]:
        base = super().info()
        base["favourite_toy"] = self.favourite_toy
        base["indoor_only"] = self.indoor_only
        return base


class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = dict()
        self.adoptions: dict[str, str] = dict()

    def add(self, animal: Animal) -> None:
        if animal.id not in self.animals:
            self.animals[animal.id] = animal
    
    def get(self, animal_id : str) -> Animal|None:
        return self.animals[animal_id] if animal_id in self.animals else None
    
    def list_all(self) -> list[Animal]:
        return list(self.animals.values())
    
    def is_adopted(self, animal_id : str) -> bool|str:
        return animal_id in self.adoptions if animal_id in self.animals else "The animal is not present in the shelter!"
    
    def set_adopted(self, animal_id : str, adopter_name : str) -> None:
        if animal_id in self.animals:
            if not self.is_adopted(animal_id):
                self.adoptions[animal_id] = adopter_name
                return adopter_name
            
            else:
                self.adoptions[animal_id] = adopter_name
                # "The animal has already been adopted. The adopter has changed"
                return adopter_name

        else:
            return "The animal is not present in the shelter!"


kuma: Cat = Cat("Kuma", 1, 13, "Walnut", True)
nebbia: Dog = Dog("Nebbia", 17, 5, "a")

sh: Shelter = Shelter()
sh.add(kuma)
sh.add(nebbia)

# print(sh.set_adopted("c0", "Cristiano"))
# print(sh.set_adopted("c0", "Mortadella"))
# print(sh.set_adopted("c10", "Mortadella"))
# print(sh.adoptions)

from flask import Flask, jsonify, request, url_for
app = Flask(__name__)

@app.route("/")
def description() -> dict:
    return jsonify({
        "description" : "Welcome to Animal Shelter API",
        "_links" : {
                    "list animals" : {"endpoint" : url_for("list_animals"), "method" : "GET"}, 
                    "sample dog" : {"endpoint" : url_for("get_animal", animal_id = "d1"), "method" : "GET"},
                    "get food of an animal" : {"endpoint" : url_for("get_food", animal_id = "d1"), "method" : "GET"},
                    "get adoption of an animal" : {"endpoint" : url_for("get_adoption", animal_id = "d1"), "method" : "GET"},
                    "add animal" : {"endpoint" : url_for("post_animal"), "method" : "POST"},
                    "add adoption for an animal" : {"endpoint" : url_for("post_adoption", animal_id = "d1"), "method" : "POST"}
                    }
            })

@app.route("/animals", methods = ['GET'])
def list_animals() -> dict:
    return jsonify({animal.id : animal.info() for animal in sh.list_all()}), 200

@app.route("/animals/<string:animal_id>", methods = ['GET'])
def get_animal(animal_id : str) -> dict:
    if sh.get(animal_id) is not None:
        return jsonify(sh.get(animal_id).info())
    else:
        return "Not found", 404

@app.route("/animals/<string:animal_id>/food", methods = ['GET'])
def get_food(animal_id : str) -> dict:
    if sh.get(animal_id) is not None:
        return jsonify({"id" : animal_id, "daily_food_grams" : sh.get(animal_id).daily_food_grams()})
    else:
        return "Not found", 404
    

@app.route("/animals/<string:animal_id>/adoption", methods = ['GET'])
def get_adoption(animal_id : str) -> dict:
    if sh.get(animal_id) is not None:
        return jsonify({"id" : animal_id, "daily_food_grams" : sh.adoptions[animal_id] if animal_id in sh.adoptions else "No adoption yet"})
    else:
        return "Not found", 404

@app.route("/animals", methods = ['POST'])
def post_animal() -> dict:
    data = request.get_json()
    
    match data["species"]:
        case "dog":
            new_animal : Dog = Dog(data["name"], data["age_years"], data["weight_kg"], data["breed"], data["is_trained"])

        case "cat":
            new_animal : Cat = Cat(data["name"], data["age_years"], data["weight_kg"], data["favourite_toy"], data["indoor_only"])
    
        case _:
            return "No specie provided", 400
    
    sh.add(new_animal)
    return jsonify({
        "_links": {
            "endpoint": url_for("get_animal", animal_id=new_animal.id),
            "method": "GET"
        },
        "animal_id": new_animal.id
    }), 201
    

@app.route("/animals/<string:animal_id>/adoption", methods = ['POST'])
def post_adoption(animal_id : str) -> dict:
    data = request.get_json()

    if animal_id in sh.animals:
        return jsonify({
            "id" : animal_id,
            "adopter" : sh.set_adopted(animal_id, data["adopter_name"]),
            "_links" : {
                    "get animal" : {
                        "endpoint" : url_for("get_animal", animal_id = animal_id),
                        "method" : "GET"
                    },

                    "get adoption" : {
                        "endpoint" : url_for("get_adoption", animal_id = animal_id),
                        "method" : "GET"
                    }
                }
            })

    else:
        return "The animal is not present in the shelter!", 404

    