'''9-3. Users: Make a class called User.
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
'''

class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs
    
    def describe_user(self) -> None:
        print(f"Name: {self.first_name} {self.last_name}\n\n--Additional informations:--")
        for k, w in self.kwargs.items():
            print(f"{k}: {w}")
    def greet_user(self) -> None:
        print(f"Hey {self.first_name}. Welcome to my program!")

person_1 = User("Lilly", "Coin", Age=23, Gender="female")
person_1.describe_user()
person_1.greet_user()

person_2 = User("Michael", "Cob", Age=25)
person_2.describe_user()
person_1.greet_user()

person_1 = User("Paol", "Bush")
person_1.describe_user()
person_1.greet_user()