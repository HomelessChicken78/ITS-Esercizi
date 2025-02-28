'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.
  Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''

#Making the list for the kind of pizza
pizza_names: list[str] = ["Margherita", "4 Stagioni", "Diavola"]

friend_pizza = pizza_names

pizza_names.append("Peperoni")
friend_pizza.append("Mushrooms")

#Print the first list
print("My favourite pizzas are: ", end="")
for pizza in pizza_names:
    print(pizza, end=", ")

#Print the second one
print("\n\nMy friend's favorite pizzas are: ", end="")
for pizza in friend_pizza:
    print(pizza, end=", ")