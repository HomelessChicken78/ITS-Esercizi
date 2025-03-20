#Dal file "persona.py" importa la classe "Persona"
from persona import Persona

#Creo una persona
cc: Persona = Persona("Cristiano", "Coccia", 21)

# print(cc)

# print(cc.name, cc.lastname, cc.age)

#Richiamare la funzione "displayData" della classe "Persona" per mostrare in output i dati relativi alla persona 'cc'
cc.displayData()

