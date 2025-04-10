class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.setName(name)
        self.setSurname(surname)
        self.setAge(age)
    
    #For the name
    def setName(self, name: str) -> None:
        if name:
            self.name = name
        else:
            raise ValueError("\n\nThe name cannot be an empty string!")
    
    def getName(self) -> str:
        return self.name
    
    #For the surname
    def setSurname(self, surname: str) -> None:
        if surname:
            self.surname = surname
        else:
            raise ValueError("\n\nThe name cannot be an empty string!\n")
    
    def getSurname(self) -> str:
        return self.surname    
    
    #For the age
    def setAge(self, age: int) -> None:
        if age >= 0 and age < 140:
            self.age = age
        elif age < 0:
            raise ValueError("\n\nAge cannot be a negative number!\n")
        else:
            raise ValueError("\n\nThe person is too old! You are lying for sure >=|\n")
    
    def getAge(self) -> int:
        return self.age
    
    def __str__(self) -> str:
        if self.age != 1:
            return f"Name: \t\t{self.name}\nSurname: \t{self.surname}\nAge: \t\t{self.age} years old"
        else:
            return f"Name: \t\t{self.name}\nSurname: \t{self.surname}\nAge: \t\t{self.age} year old"
    
    def __repr__(self) -> tuple[str, str, int]:
        return (self.name, self.surname, self.age)
    
    def __call__(self) -> None:
        if self.age < 18:
            print(f"{self.name.title()} è minorenne")
        elif self.age >= 18 and self.age < 30:
            print(f"{self.name.title()} è maggiorenne")
        elif self.age >= 30 and self.age < 80:
            print(f"{self.name.title()} è una persona adulta")
        else:
            print(f"{self.name.title()} è una persona anziana")