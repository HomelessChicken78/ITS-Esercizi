from classi import *

# doc1: Documento = Documento("Ciao ciao")
# print(doc1.isInText("gooo"))
# print(doc1.isInText("Ciao"))

mail: Email = Email("Ciao", "ciao@me.it", "iosono@it.it", "C")
print(mail.getText())
mail.writeToFile("./email.txt")

print("\n-------------------------------------------------\n")
f: File = File("./documenti/document.txt")
print("Ecco il metodo leggiTestoDaFile():")
print(f.getText())
print()