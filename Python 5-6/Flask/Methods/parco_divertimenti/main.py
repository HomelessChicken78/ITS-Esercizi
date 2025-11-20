from abc import ABC, abstractmethod
from typing import Self

class Ride(ABC):
    
    ids: dict[int, Self] = dict()

    def __init__(self, name : str, min_height_cm : int):
        self.id = max(Ride.ids.keys()) + 1 if len(Ride.ids) > 0 else 0
        self.name = name
        self.min_height_cm = min_height_cm

        Ride.ids[self.id] = self

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    @abstractmethod
    def info(self) -> dict[str, int|str]:
        return {
            "id" : self.id,
            "name" : self.name,
            "min_height_cm" : self.min_height_cm,
            "categoria" : self.category()
        }
    
    @abstractmethod
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return round(self.base_wait() * crowd_factor)


class RollerCoaster(Ride):
    def __init__(self, name : str, min_height_cm : int, inversions : int):
        super().__init__(name, min_height_cm)
        self.inversions = inversions
    
    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 40
    
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return super().wait_time(crowd_factor)
    
    def info(self) -> dict[str, int|str]:
        return {
            "id" : self.id,
            "name" : self.name,
            "min_height_cm" : self.min_height_cm,
            "categoria" : self.category(),
            "inversions" : self.inversions
        }


class Carousel(Ride):
    def __init__(self, name : str, min_height_cm : int, animals : list[str]):
        super().__init__(name, min_height_cm)
        self.animals = animals[:]
    
    def category(self) -> str:
        return "family"

    def base_wait(self) -> int:
        return 10
    
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return super().wait_time(crowd_factor)
    
    def info(self) -> dict[str, int|str]:
        return {
            "id" : self.id,
            "name" : self.name,
            "min_height_cm" : self.min_height_cm,
            "categoria" : self.category(),
            "animals" : self.animals
        }

class Park:
    def __init__(self) -> None:
        self.rides: dict[int, Ride] = dict()
    
    def add(self, ride : Ride) -> Ride:
        if ride.id not in self.rides:
            self.rides[ride.id] = ride
        else:
            raise ValueError("Error: Ride already present in the park")
        return {ride.id : ride.info()}

    def get(self, ride_id) -> Ride|None:
        if ride_id in self.rides:
            return self.rides[ride_id]
        else:
            return None
    
    def list_all(self) -> list[Ride]:
        return list(self.rides.values())


r1 : RollerCoaster = RollerCoaster("Hihihihaw ride", 200, 6)
r2 : RollerCoaster = RollerCoaster("The Fool's Foolery", 450, 14)
a1 : Carousel = Carousel("Coccodrillini's come fa", 10, ["Coccodrillo", "Coccodrillo", "Coccodrillo", "Python"])

park : Park = Park()
park.add(r1)
park.add(r2)
park.add(a1)
# print(park.get(0).name)
# print(park.list_all())

from flask import Flask, jsonify, url_for
app = Flask(__name__)

@app.route("/", methods=['GET'])
def description() -> dict[str, str]:
    return jsonify({
        "description" : "Welcome to Park API",
        "_links" : {
                    "/rides" : url_for("list_rides"), 
                    "/rides/1" : url_for("get_ride", ride_id = 1),
                    "/rides/1/wait/4.0" : url_for("get_wait_ride", ride_id = 1 , crowd = 4.0)
                    }
            })

@app.route("/rides", methods=['GET'])
def list_rides() -> list[dict[str, str|int]]:
    new_lst: list[dict[str, str|int]] = []

    for v in park.rides.values():
        new_lst.append(v.info())
    
    return jsonify(new_lst), 200

@app.route("/rides/<int:ride_id>")
def get_ride(ride_id : int) -> dict:
    return jsonify(park.get(ride_id).info()) if park.get(ride_id) is not None else jsonify({}), 404

@app.route("/rides/<int:ride_id>/wait/<float:crowd>")
def get_wait_ride(ride_id : int, crowd : float = 1.0) -> dict:
    return jsonify({"wait time" : park.get(ride_id).wait_time(crowd)}), 200

@app.route("/rides/<int:ride_id>/wait/")
def get_wait_ride_2(ride_id : int) -> dict:
    return jsonify({"wait time" : park.get(ride_id).wait_time()}), 200