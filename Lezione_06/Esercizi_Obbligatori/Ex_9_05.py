'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method
called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call
increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.'''

class User:
    def __init__(self, first_name: str, last_name: str, login_attempts: int = 0, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.kwargs = kwargs


    def incremet_login_attempts(self) -> None:
        self.login_attempts += 1
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0
    
    def describe_user(self) -> None:
        print(f"Name: {self.first_name} {self.last_name}\n\n--Additional informations:--")
        for k, w in self.kwargs.items():
            print(f"{k}: {w}")
    def greet_user(self) -> None:
        print(f"Hey {self.first_name}. Welcome to my program!")

if __name__ == "__main__":
    person_1 = User("Lilly", "Coin", Age=23, Gender="female")
    for attempt in range(0, 4):
        person_1.incremet_login_attempts()
    print(person_1.login_attempts)
    person_1.reset_login_attempts()
    print(person_1.login_attempts)
