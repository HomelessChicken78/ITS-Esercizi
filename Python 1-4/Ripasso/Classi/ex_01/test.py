from Contacts import ContactManager

c: ContactManager = ContactManager()
# ATTENZIONE: TUTTI I NUMERI IN QUESTO FILE DRIVER SONO FALSI!

print(c.create_contact("giAComo", ["+39 23178647", "+39 777 936 6483"]))
print(c.create_contact("Giacomo", ["+39 23178647", "+39 777 936 6483"]))

print(c.list_contacts())

print("\n-- Listing phone numbers: --")
print(c.list_phone_numbers("Giacomo"))
# same as print(c.list_phone_numbers("giaCOmo"))
print(c.list_phone_numbers("Francesco"), "\n")

print("Aggiungi un numero a Gilberto:", c.add_phone_number("Gilberto", "123768"))
print("Aggiungi un numero a Giacomo:", c.add_phone_number("GiacoMo", "+39 23178647"))
print("Aggiungi un numero a Giacomo:", c.add_phone_number("GiacoMo", "+39 231"))

print()
print("Rimuovo un numero  di Gilberto: ", c.remove_phone_number("Gilberto", "7231968"))
print("Rimuovo un numero  di Giacomo: ", c.remove_phone_number("Giacomo", "7231968"))
print("Rimuovo un numero  di Giacomo: ", c.remove_phone_number("Giacomo", "+39 231"))

print()
print("Aggiornando un numero di Gilberto:", c.update_phone_number("Gilberto", "438972", "214897"))
print("Aggiornando un numero di Gilberto:", c.update_phone_number("Giacomo", "+39 893 123 5494", "+39 381 533 9102"))
print("Aggiornando un numero di Gilberto:b", c.update_phone_number("Giacomo", "+39 23178647", "+39 381 533 9102"))

print()
c.create_contact("Francesco", ["+35 481 328 1273", "+39 777 936 6483", "+38 849 129 3478"])
c.create_contact("Rachele", ["+39 172 385 3922","+39 982 284 7752","+39 777 936 6483","+39 444 562 4724"])
c.create_contact("Luca", ["+39 124 976 6454"])
print(c.search_contact_by_phone_number("+39 777 936 6483"))
print(c.search_contact_by_phone_number("+38 87132 84"))