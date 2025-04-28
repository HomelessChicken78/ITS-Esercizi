from persona import Person
from alieno import Alien


# Create an object p of the class Person
p: Person = Person("Cristiano", "Coccia", 21)

# Let's see the information of the person "p"
print(p)

# Create an object "et" of the class Alien
et: Alien = Alien("Andromeda")

# Let's see the information of the alien "et"
print(et)

# The object p invoke the method "speak"
p.speak()

# The object et invoke the method "speak"
et.speak()