class Person:  #NOTÈ: Camel Case is the convention here.
    #This is the constructor, which allows us to  initialize each object of the class
    def __init__(self, first_name, last_name, age):  #'Self' is a keyword that reference the object we are currently using/creating. It takes the memory ID of the current object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person_1: Person = Person("Eric", "Crow", 45)  #Yes, we could technically say that a class is a new type of data

'''Additional Information: each object has a different place in the memory and that is how two objects are dinsticted.
That means that even if two objects have the same attributes, for python they are technically different'''