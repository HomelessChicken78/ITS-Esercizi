# Very cool what we saw, but it is not the best way to do it. We have to remember to always close files
f1 = open("folder_1/Hello_World.txt", "r")
# This allows to always close the file, regardless of exceptions
try:
   print(f1.read())
finally:
    f1.close()

# We can also use "with". This as a __exit__ that auto-closes the file
with open("folder_1/Hello_World.txt", "r") as f1:
    print(f1.read())