'''Exercise 3-7
Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the
end of your program.'''

guests: list[str] = ["Albert Einstein", "Melon Musk", "Steve Jobs", "Pingproxy", "Quandale Dingle", "Goofy Goof", "Tizio Caio"]

'''WITH FOR
for i in guests:
    print(f"Hey {i} wanna come to my party?")'''

'''WITHOUT FOR'''
print(f"Hey {guests[0]} wanna come to my party?")
print(f"Hey {guests[1]} wanna come to my party?")
print(f"Hey {guests[2]} wanna come to my party?")
print(f"Hey {guests[3]} wanna come to my party?")
print(f"Hey {guests[4]} wanna come to my party?")
print(f"Hey {guests[5]} wanna come to my party?")
print(f"Hey {guests[6]} wanna come to my party?")

print(f"\n{guests[5]} couldn't make it to the party! :(\n")
guests[5] = "Mickey Mouse"

'''WITH FOR
for i in guests:
    print(f"Hello {i}, would you like to come to my party?")'''

'''WITHOUT FOR'''
print(f"Hello {guests[0]}, would you like to come to my party?")
print(f"Hello {guests[1]}, would you like to come to my party?")
print(f"Hello {guests[2]}, would you like to come to my party?")
print(f"Hello {guests[3]}, would you like to come to my party?")
print(f"Hello {guests[4]}, would you like to come to my party?")
print(f"Hello {guests[5]}, would you like to come to my party?")
print(f"Hello {guests[6]}, would you like to come to my party?")

print("\nGUYS I FOUND A BIGGER TABLE!!!\n")
guests.insert(0, "Leandro Pazienza")
guests.insert(len(guests)//2, "Pikachu")
guests.append("Socrate")

'''WITH FOR
for i in guests:
    print(f"Hi {i}. You are invited to my party!")'''

'''WITHOUT FOR'''
print(f"Hi {guests[0]}. You are invited to my party!")
print(f"Hi {guests[1]}. You are invited to my party!")
print(f"Hi {guests[2]}. You are invited to my party!")
print(f"Hi {guests[3]}. You are invited to my party!")
print(f"Hi {guests[4]}. You are invited to my party!")
print(f"Hi {guests[5]}. You are invited to my party!")
print(f"Hi {guests[6]}. You are invited to my party!")
print(f"Hi {guests[7]}. You are invited to my party!")
print(f"Hi {guests[8]}. You are invited to my party!")
print(f"Hi {guests[9]}. You are invited to my party!")

print("\nMy table won't arrive in time guys! I only got space for two guests :(")
while (len(guests) > 2):
    print(f"I am sorry {guests[len(guests) - 1]}, i cannot invite you to the party anymore")
    guests.pop(len(guests) - 1)

print("\n")
for i in guests:
    print(f"Hi {i}, you are still in!!!")

guests.remove("Leandro Pazienza")
guests.remove("Albert Einstein")
print(guests)