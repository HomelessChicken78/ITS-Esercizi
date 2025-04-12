'''r5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''

#Make a list with the current existing users already registered
current_users: list[str] = [
    "Alan",
    "Francis",
    "jerry",
    "Nicol",
    "Luigi",
    "Ilary",
    "CarmEN",
    "Katerine",
    "RYAN"
    ]

#Make a copy of the list where each user is instead in lowercase
current_users_lower: list[str] = []
for users in current_users:
    current_users_lower.append(users.lower())

#Make a list containing the users that want to register to the website
new_users: list[str] = [
    "Vicky",
    "Jerry",
    "Penny",
    "Carmen",
    "Ryan"
]

#Check whether the name already exists or not
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The name {user} has already been taken. Try with another name.")
    else:
        print(f"The name {user} is avaible!")