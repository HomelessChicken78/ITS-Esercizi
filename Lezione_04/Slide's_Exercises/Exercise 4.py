'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5'''

def check_each(nums: list[int]) -> None:
    for n in nums:
        if n > 5:
            print(f"The number {n} is bigger than 5")
        elif n < 5:
            print(f"The number {n} is smaller than 5")
        else:
            print(f"The number {n} is equal to 5")

'''Output Check
check_each([42, 42, 3, 7, 1, 0, -2, 5])'''