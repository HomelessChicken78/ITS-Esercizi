'''r5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.'''

#Create the list
names: list[str] = ["Kate", "Melinda" "Rosa", "Pablo", "admin", "Lucrezia", "Haida"]

#Remove all users from it
del names[:]

#Print the message for everyone
if len(names) > 0:
    for person in names:
        if person == "admin":
            print("Welcome admin!\nHere you can manage the access of other users or see the status report")
        else:
            print(f"Welcome {person}.\nYou are currently logged in!")
        print("-----------------------------------------------------------------------")
else:
    print("We need to find some users!")