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

num_system: str = input("Type the characters that the number system is composed of. The order matters!:\n>\t")