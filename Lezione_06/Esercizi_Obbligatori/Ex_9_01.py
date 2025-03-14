'''9-1. Restaurant: Make a class called Restaurant.
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) -> None:
        print(f"The restaurant \"{self.restaurant_name}\" is a {self.cuisine_type} restaurant")
    
    def open_restaurant(self) -> None:
        print(f"The restaurant \"{self.restaurant_name}\" is now open to public!")

ITS_Bakery: Restaurant = Restaurant("ITS BAKERY", "Italian")
print(ITS_Bakery.restaurant_name, "\n", ITS_Bakery.cuisine_type)
ITS_Bakery.describe_restaurant()
ITS_Bakery.open_restaurant()
