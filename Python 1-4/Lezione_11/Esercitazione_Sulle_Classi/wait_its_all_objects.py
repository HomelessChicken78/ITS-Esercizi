# Wait it's all objects? Always has been

class Classe1:
    pass
print(type(Classe1))
def Funct1():
    pass
print(type(Funct1))

print(type(print))

import numpy
print(type(numpy))

with open("wait_its_all_objects.py", "r") as f:
    print(type(f))

print(type(...))

print(type(None))

print("<class 'Exception'>" if isinstance(ValueError(), Exception) else "")

print(type(type))

print(type(slice(0, 4)))  # e.g. list[:4]. That [:4] is an object