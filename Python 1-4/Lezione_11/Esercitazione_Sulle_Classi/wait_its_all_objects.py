# Wait it's all objects? Always has been

print(type(int()), type(float()), type(bool()), type(str()), type(list()), type(frozenset()), type(set()), type(dict()), type(tuple()))
print(type(None))
print(type(...))
print(type(slice(0, 4)))  # e.g. list[:4]. That [:4] is an object

print(type(int), type(float), type(bool), type(str), type(list), type(frozenset), type(set), type(dict), type(tuple))

def Funct1():
    pass
print(type(Funct1))

print(type(print))

print(type(type))

import numpy
print(type(numpy))

class Classe1:
    pass
print(type(Classe1))

with open(__file__, "r") as f:
    print(type(f))

print("<class 'Exception'>" if isinstance(ValueError(), Exception) else "")