#Dal file "persona.py" importa la classe "Persona"
from persona import Persona

#Creo una persona
cc: Persona = Persona("Cristiano", "Coccia", 21)

print(cc)

print(cc.name, cc.lastname, cc.age)