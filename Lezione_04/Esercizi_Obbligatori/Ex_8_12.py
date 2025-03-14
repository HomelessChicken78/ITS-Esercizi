'''8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time.'''

def make_sandwich(*ingredients) -> None:
    print("Your sandwitch contains:")
    for item in ingredients:
        print(item)

make_sandwich("Lettuce", "Cheese", "Prosciutto")
print("\n---------------------------------------------------\n")
make_sandwich("Tonno")
print("\n---------------------------------------------------\n")
make_sandwich("Mortadella", "Salad")