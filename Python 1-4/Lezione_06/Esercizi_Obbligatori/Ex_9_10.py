'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.'''

from Ex_9_04 import Restaurant
Jap: Restaurant = Restaurant("Celeste", "Japanese")
Jap.describe_restaurant()