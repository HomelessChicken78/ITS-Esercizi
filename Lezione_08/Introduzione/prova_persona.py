from persona import Person

cc: Person = Person("hi", "hi", 3)
cc.setAge(1)
print(cc.getAge())
# cc.setName("")
cc.setName("Cristiano")
cc.setSurname("Coccia")

# cc.setAge(140)
cc()
print(cc, "\n\n-------------------------\n")
cc.setAge(21)
cc()
print(cc)
print(cc.__repr__())