'''EXercise 3-6
More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

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