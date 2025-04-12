# #Dal file "persona.py" importa la classe "Persona"
# from persona import Persona

# #Creo una persona
# cc: Persona = Persona("Cristiano", "Coccia", 21)

# # print(cc)

# # print(cc.name, cc.lastname, cc.age)

# #Richiamare la funzione "displayData" della classe "Persona" per mostrare in output i dati relativi alla persona 'cc'
# cc.displayData()

#Dal file "persona2" importa la classe "Persona"
from persona2 import Persona

cc: Persona = Persona()

#Richiamo la funzione "displayData" della classe "Persona" per mostrare in output i dati relativi all'oggetto 'cc'
cc.displayData()

#Modificare il nome della persona 'cc'
cc.setName("Cristiano")

print("---------------------")

cc.displayData()

#Modificare il cognome della persona 'cc'
cc.setLastname("Coccia")

#Modifica l'età della persona 'cc'
cc.setAge(21)

print("---------------------")

cc.displayData()

print("---------------------")
print(cc.getName(), cc.getLastname(), cc.getAge())