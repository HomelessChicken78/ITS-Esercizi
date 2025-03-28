'''Exercise 3-5
Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list."'''

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