'''9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a
default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant
has served, and then change this value and print it again. Add a method called set_number_served() that lets you set
the number of customers that have been served. Call this method with a new number and print the value again. Add a
method called increment_number_served() that lets you increment the number of customers who’ve been served. Call
this method with any number you like that could represent how many customers were served in, say, a day
of business. '''

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served:int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_server(self, number_server: int) -> None:
        self.number_served = number_server
    
    def increment_number_served(self, increment: int = 1) -> None:
        self.number_served += increment
    
    def describe_restaurant(self) -> None:
        print(f"The restaurant \"{self.restaurant_name}\" is a {self.cuisine_type} restaurant")
    
    def open_restaurant(self) -> None:
        print(f"The restaurant \"{self.restaurant_name}\" is now open to public!")

if __name__ == "__main__":
    ITS_Bakery: Restaurant = Restaurant("ITS BAKERY", "Italian")
    print(f"{ITS_Bakery.restaurant_name} has server {ITS_Bakery.number_served} people today")
    ITS_Bakery.set_number_server(38)
    print(f"{ITS_Bakery.restaurant_name} has server {ITS_Bakery.number_served} people today")
    ITS_Bakery.increment_number_served(4)
    print(f"{ITS_Bakery.restaurant_name} has server {ITS_Bakery.number_served} people today")
