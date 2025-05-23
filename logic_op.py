from typing import Callable
from typing import Any

def repeat_until(action:object|Callable, condition:bool|Callable, *action_param):
    while True:
        if action_param:
            action(*action_param)
        else:
            action()
        if condition():
            break

def xor(obj1: Any, obj2: Any) -> bool:
    '''xor logic gate. Behaviour can be customized in a special method called __xor__'''
    if hasattr(obj1, "__xor__") and callable(getattr(obj1, "__xor__")):
        return obj1.__xor__(obj2)
    return (obj1 or obj2) and not (obj1 and obj2)
    
def nand(obj1: Any, obj2:Any) -> bool:
    '''nand logic gate. Behaviour can be customized in a special method called __nand__'''
    if hasattr(obj1, "__nand__") and callable(getattr(obj1, "__nand__")):
        return obj1.__nand__(obj2)
    return not(obj1 and obj2)

def nor(obj1: Any, obj2: Any) -> bool:
    '''nor logic gate. Behaviour can be customized in a special method called __nor__'''
    if hasattr(obj1, "__nor__") and callable(getattr(obj1, "__nor__")):
        return obj1.__nor__(obj2)
    return not(obj1 or obj2)

def xnor(obj1: Any, obj2: Any) -> bool:
    '''xnor logic gate. Behaviour can be customized in a special method called __xnor__'''
    if hasattr(obj1, "__xnor__") and callable(getattr(obj1, "__xnor__")):
        return obj1.__xnor__(obj2)
    return not((obj1 or obj2) and not (obj1 and obj2))



def test(obj:object):
    # Try to check if the object passed has a parameter has got a __test__ method. If it does, it calls it.
    if hasattr(obj, "__test__") and callable(getattr(obj, "__test__")):
        obj.__test__()
    else:
        raise AttributeError(f"type object '{obj.__name__}' has no attribute '__test__'")

class Operators:
    xor = xor
    nand = nand
    nor = nor
    xnor = xnor

# if __name__ == "__main__":
    # i = [0]
    # def counter(n):
    #     i[0] += n
    #     print(i[0])
    
    # def done():
    #     return i[0] > 6
    # repeat_until(counter, done, 2)

    # print(xor(False, False))  # False
    # print(xor(True, False))  # True
    # print(xor(False, True))  # True
    # print(xor(True, True))  # False

    # print(nand(False, False))  # True
    # print(nand(True, False))  # True
    # print(nand(False, True))  # True
    # print(nand(True, True))  # False

    # print(nor(False, False))  # True
    # print(nor(True, False))  # False
    # print(nor(False, True))  # False
    # print(nor(True, True))  # False

    # print(xnor(False, False))  # True
    # print(xnor(True, False))  # False
    # print(xnor(False, True))  # False
    # print(xnor(True, True))  # True

    # class ciao:
    #     def __test__():
    #         print("Hi")
    # test(ciao)
    # # test(int)

    # class custom_operators:
    #     def __init__(self, v: int):
    #         self.value = v

    #     def __xor__(self, other) -> str:
    #         return "I love xor"
        
    #     def __nand__(self, other) -> str:
    #         return "bob"
        
    #     def __nor__(self, other):
    #         return other
        
    #     def __xnor__(self, other):
    #         return self.value > other

    # a = custom_operators(4)
    # print(xor(a, True))
    # print(nand(a, True))
    # print(nor(a, "i am other"))
    # print(xnor(a, 100))