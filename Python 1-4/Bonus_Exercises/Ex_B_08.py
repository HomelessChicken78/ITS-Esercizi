''' 
Allowed functions : None
Create an iterated function that returns a number. This number is the result of a
factorial operation based on the number given as a parameter.
 If the argument is not valid the function should return 0
 Here’s how it should be prototyped:
 def ft_iterative_factorial(nb: int) -> int:'''

def ft_iterative_factorial(nb: int) -> int:
    if (not isinstance(nb, int)) or nb <= 0:
        return 0
    if nb > 1:
        return nb*ft_iterative_factorial(nb - 1)
    else:
        return 1

#Output Check    
print(ft_iterative_factorial(5))