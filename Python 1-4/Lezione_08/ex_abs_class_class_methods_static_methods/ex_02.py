'''Exercise 2: Implementing Static Methods

Create a class called MathOperations to group together some basic arithmetic functionality. Inside this class, define
two static methods:

    add, which accepts two numeric parameters and returns their sum.

    multiply, which also takes two numeric parameters and returns their product.

Finally, write a small driver program to test the functionality of the add and multiply methods. This should involve
calling both methods with sample inputs and printing the results to verify that they work correctly.'''

class MathOperations:
    @staticmethod
    def add(n1: int|float, n2: int|float) -> int|float:
        return n1 + n2
    
    @staticmethod
    def multiply(n1: int|float, n2: int|float) -> int|float:
        return n1 * n2

if __name__ == "__main__":
    print(MathOperations.add(1, 4))
    print(MathOperations.multiply(1, 4))