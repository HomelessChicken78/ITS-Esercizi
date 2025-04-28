# ABC = Abstact Base Class
from abc import ABC, abstractmethod

class GenericShape(ABC):  # This means that the class "GenericShape" is an abstract class

    '''This class allows to visualize shapes on screen'''

    @abstractmethod  # This says "Hey, the following is an abstract method"
    def draw(self) -> None:
        pass

    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            raise ValueError("The shape cannot be an empty string!")
        
    def getShape(self) -> str:
        return self.shape