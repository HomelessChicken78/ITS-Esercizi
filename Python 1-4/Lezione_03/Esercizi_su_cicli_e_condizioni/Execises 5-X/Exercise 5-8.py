'''r5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''

#Create the list
names: list[str] = ["Kate", "Melinda" "Rosa", "Pablo", "admin", "Lucrezia", "Haida"]

#Print the message for everyone
for person in names:
    if person == "admin":
        print("Welcome admin!\nHere you can manage the access of other users or see the status report")
    else:
        print(f"Welcome {person}.\nYou are currently logged in!")
    print("-----------------------------------------------------------------------")