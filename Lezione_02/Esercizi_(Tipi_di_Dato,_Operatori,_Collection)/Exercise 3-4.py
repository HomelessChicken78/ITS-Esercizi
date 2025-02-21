'''Exercise 3-4
Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.'''

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
