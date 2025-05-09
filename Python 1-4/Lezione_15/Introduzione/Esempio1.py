PATH: str = "folder_1/Hello_World.txt"
open(PATH, "w").write("Hello World")

file1 = open(PATH) # Open a file
print("Here is the header:", file1)  # This end up printing the header of the file, not the content itself
print("\nHere is the content of the file:\n-----------------\n", file1.read(),"\n-----------------\n") # To Read the content and print it

file1.close() # Now let's close the file

# Let's see what happens if we try to read the file now
print("Reading the file...")
try:
    file1.read() # This gives an error, since the file has been closed
except ValueError:
    print("I don't know that file\n")
else:
    print(file1.read())

# Let's try to write on it
file1 = open(PATH)
print("Writing on the file \"hi\"...")
try:
    file1.write("hi") # This gives an error, since the file has been opened in "read" mode
except IOError:
    print("Cannot open the file, it has been opened in reading mode")
else:
    print("Done!")
    file1.close()
    print("\nHere is the content of the file:\n-----------------\n", file1.read(),"\n-----------------\n")
file1.close()

# Ok, so let's open it in "write mode" first
file1 = open(PATH, "w")
print("\nWriting on the file \"hi\"...")
try:
    file1.write("hi")
except IOError:
    print("Cannot open the file, it has been opened in reading mode")
else:
    print("Done!")
    file1.close()
    print("\nHere is the content of the file:\n-----------------\n", open(PATH, "r").read(),"\n-----------------\n")

# But what if i don't want to overwrite the file?
file1 = open(PATH, "a")  # This means append
print("\nAppending on the file \", my name is Cristiano\"...")
try:
    file1.write(", my name is Cristiano")
except IOError:
    print("Cannot open the file, it has been opened in reading mode")
else:
    print("Done!")
    file1.close()
    print("\nHere is the content of the file:\n-----------------\n", open(PATH, "r").read(),"\n-----------------\n")