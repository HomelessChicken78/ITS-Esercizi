class  User:
    def __init__(self, first_name: str="", last_name: str="", username: str="", email: str="@.com"):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        
    def describe_user(self) -> None:
        print(f"{self.first_name} {self.last_name} informations:\nUsername: {self.username}\nEmail: {self.email}")

    def greet_user(self) -> None:
        print(f"Hey {self.first_name}. Welcome to my program!")

class Privileges:
    def __init__(self, priv: list[str]):
        self.priv = priv
    
    def show_privileges(self) -> None:
        print(", ".join(self.priv))

class Admin:
    def __init__(self, user: User, priv: Privileges):
        self.user = user
        self.priv = priv
        

if __name__ == "__main__":
    p1: Privileges = Privileges(["1", "2", "3"])
    p1.show_privileges()