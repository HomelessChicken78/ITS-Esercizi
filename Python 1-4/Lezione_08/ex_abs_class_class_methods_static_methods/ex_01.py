'''Exercise 1: Creating an Abstract Class with Abstract Methods

Start by defining an abstract base class called Shape. This class should include two abstract methods: one named
area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate
the perimeter. Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a
blueprint for all shapes that will inherit from it.

Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these
subclasses must provide their own implementation of the area and perimeter methods, based on the geometric
formulas appropriate to their shapes.

Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and
perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.r = radius
    
    def rad(self) -> float:
        return self.r

    def area(self) -> float:
        return pi*(self.rad()**2)
    
    def perimeter(self) -> float:
        return 2*pi*self.rad()

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.l = length
        self.w = width
    
    def len(self) -> float:
        return self.l
    
    def wid(self) ->  float:
        return self.w
    
    def area(self) -> float:
        return self.wid() * self.len()
    
    def perimeter(self):
        return 2 * (self.wid() + self.len())
    
if __name__ == "__main__":
    circle1: Circle = Circle(3)
    print(circle1.area())
    print(circle1.perimeter())

    rectangle1: Rectangle = Rectangle(3, 3)
    print(rectangle1.area())
    print(rectangle1.perimeter())