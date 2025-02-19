'''EXercise 3-6
More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

guests: list = ["Albert Einstein", "Melon Musk", "Steve Jobs", "Pingproxy", "Quandale Dingle", "Goofy Goof", "Tizio Caio"]
for i in guests:
    print(f"Hey {i} wanna come to my party?")

print(f"\n{guests[5]} couldn't make it to the party! :(\n")
guests.remove("Goofy Goof")

guests.append("Mickey Mouse")
for i in guests:
    print(f"Hello {i}, would you like to come to my party?")

print("\nGUYS I FOUND A BIGGER TABLE!!!\n")
guests.insert(0, "Leandro Pazienza")
guests.insert(len(guests)//2, "Pikachu")
guests.append("Socrate")

for i in guests:
    print(f"Hi {i}. You are invited to my party!")