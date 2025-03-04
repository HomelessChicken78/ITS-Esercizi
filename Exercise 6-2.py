'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.'''

fav_num: dict[str, int] = {
    "Larry" : 42,
    "Olga" : -35,
    "Livio" : 9,
    "Francy" : 3, 
    "Alex" : 7,
    "Lois" : 77,
    "Raimondo" : 12,
    "Mike" : 42,
    "Grace" : 5,
    "Maggie" : 24
    }

for person, num in fav_num.items():
    print(f"{person}'s favourite number is: {num}.")