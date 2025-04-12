'''r5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list.
If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''

favourite_fruits: list[str] = ["orange", "banana", "watermelon"]

if "apple" in favourite_fruits:
    print("You really like Apples")
if "pear" in favourite_fruits:
    print("You enjoy eating Pears")
if "banana" in favourite_fruits:
    print("Either you are a minion from despicable me or you are a monkey, 'cause you like Bananas")
if "orange" in favourite_fruits:
    print("One of your favourite are Oranges")
if "watermelon" in favourite_fruits:
    print("Wow! You really like Watermelons, don't you?")