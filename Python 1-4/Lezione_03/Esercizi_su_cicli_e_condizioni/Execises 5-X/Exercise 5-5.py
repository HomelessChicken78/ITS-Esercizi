'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_color: str = "green"  #Version where it runs the if
#alien_color: str = "yellow"   #Version where it runs the elif
#alien_color: str = "red"   #Version where it runs the else
points: int = 0

if alien_color == "green":
    print("You just earned 5 points for shooting the alien!")
    points += 5
elif alien_color == "yellow":
    print("You just earned 10 points!")
    points += 10
else:
    print("WOAH. You earned 15 points")
    points += 15