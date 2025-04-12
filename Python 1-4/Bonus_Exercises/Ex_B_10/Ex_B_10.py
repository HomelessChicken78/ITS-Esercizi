'''Chapter VII
Exercise 04 : ft_putnbr_base
Exercise 04
ft_putnbr_base
Turn-in directory : ex04/
Files to turn in : ft_putnbr_base.c
Allowed built-in functions: TBA
• Create a function that displays a number in a base system in the terminal.
• This number is given in the shape of an int, and the radix in the shape of a string
of characters.
• The base-system contains all useable symbols to display that number :
◦ 0123456789 is the commonly used base system to represent decimal numbers
◦ 01 is a binary base system ;
◦ 0123456789ABCDEF an hexadecimal base system ;
◦ poneyvif is an octal base system.
• The function must handle negative numbers.
• If there’s an invalid argument, an error should be displayed. Examples of invalid
arguments :
◦ base is empty or size of 1;
◦ base contains the same character twice ;
◦ base contains + or - ;
◦ base contains characters that are not alphanumerical (eg parenthesis or slashes are not allowed)'''

from B_10_Conquer.Correct_Input.n_2_0_Check_input import check_input
from B_10_Conquer.Conversion.n_4_2_from_decimal_to_other import base_conversion
from B_10_Conquer.Conversion.n_4_2_4_new_base import from_remainders_to_new_base

#Ask how the number system is composed. Force the user to make it valid
num_system: str = input("Type the characters that the number system is composed of. The order matters!:\n>\t")
while not check_input(num_system):
    print("\n---WARNING: The input is not correct. It may contain repeated or unsupported characters or the string is not long enough!---\n")
    num_system: str = input("Type the characters that the number system is composed of. The order matters!:\n>\t")

#Ask the decimal number to be converted into the new system. Force the user to insert a number and not anything else
dec_num: str = input("Insert a decimal number:\n>\t")
while not dec_num.isnumeric():
    print("\n---WARNING: The number typed is not a decimal integer number!---\n")
    dec_num: str = input("Insert a decimal number:\n>\t")
dec_num = int(dec_num)  #When the user insert a number, convert the string into an integer

base: int = len(num_system)

print(from_remainders_to_new_base(base_conversion(dec_num, base), num_system))

