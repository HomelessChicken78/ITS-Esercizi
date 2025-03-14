'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.'''

from Ex_9_01 import Restaurant

ITS_Bakery: Restaurant = Restaurant("ITS BAKERY", "Italian")
ITS_Bakery.describe_restaurant()

my_restaurant: Restaurant = Restaurant("We are cool", "Fast Food")
my_restaurant.describe_restaurant()

quaranta: Restaurant = Restaurant("Da quaranta", "Pizzeria")
quaranta.describe_restaurant()