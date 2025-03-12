'''
Allowed functions : None
Create a function ft_fibonacci that returns the n-th element of the Fibonacci
sequence, the first element being at the 0 index. We’ll consider that the Fibonacci
sequence starts like this: 0, 1, 1, 2
Here’s how it should be prototyped :
def ft_fibonacci(index: int) -> int

Obviously, ft_fibonacci has to be recursive
If the index is less than 0, the function should return -1.'''

def ft_fibonacci(index: int) -> int:
    if index > 1:
       return ft_fibonacci(index-1) + ft_fibonacci(index-2)
    elif index == 1:
        return 1
    elif index == 0:
        return 0

#Output Check
print(ft_fibonacci(int(input("Insert a number:\n>\t"))))