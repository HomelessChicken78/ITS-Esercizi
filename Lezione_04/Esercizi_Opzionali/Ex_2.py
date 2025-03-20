'''2. Guess the Number Game:
    ∙ Create a function that generates a random number within a range specified by the user.
    ∙ Prompt the user to guess the number within a specified maximum number of attempts.
    ∙ Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    ∙ Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''

from random import randint

'''This function forces the user to insert an input that is numeric'''
def input_to_int(prompt: str, error_prompt: str) -> int:
    #Ask the user the first time
    resulting_input: int = input(prompt)

    #If the input is not a number ask it again, simulating the behaviour of a repeat until
    while not resulting_input.isnumeric():
        print(error_prompt)
        resulting_input = input(prompt)
    
    resulting_input = int(resulting_input)  #Trasform the input into an integer

    return resulting_input


start: int = input_to_int("Type the first number:\n>\t", "\nWARNING: You did not type a number!!!\n")
end: int = input_to_int("Type the second number:\n>\t", "\nWARNING: You did not type a number!!!\n")

#End must be lower than the start
while end < start:
    print(f"\nWARNING: The second number must be lower than (or equal to) the second one!!! (first number was {start})\n")
    end = input_to_int("Type the second number:\n>\t", "\nWARNING: You did not type a number!!!\n")

attempt: int = 0
win: bool = False
correct_guess: int = randint(start, end)  #Generate the random number
print(f"Cheat: {correct_guess}")

while attempt < 3:
    guess: int = input_to_int(f"Type your guess (You have {3 - attempt} attempt(s)):\n>\t", "\nWARNING: You did not type a number!!!\n")  #Ask the user to make a guess
    if guess > correct_guess:
        print(f"The correct number is bigger than {guess}")
    elif guess < correct_guess:
        print(f"")
    else:
    attempt += 1
