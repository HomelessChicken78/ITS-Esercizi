'''
PARTE 1: Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail
(facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario
con i dettagli del contatto.
 
PARTE 2: Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e
cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe
aggiornare il dizionario del contatto.

For example:
contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
>>> {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
>>> {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}

print(update_contact(contact, "Mario Rossi", telefono=123456789))'''

from typing import Any

def create_contact(name: str, email: str=None, telefono: int=None) -> dict[str:Any]:
    contact: dict[str:Any] = {"profile" : name, "email" : email, "telefono" : telefono}

    return contact

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict[str:Any]:
    dictionary["profile"] = name
    if email:
        dictionary["email"] = email
    if telefono:
        contact["telefono"] = telefono
    
    return dictionary

if __name__ == "__main__":	
    contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
    print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
    print(update_contact(contact, "Mario Rossi", telefono=123456789))
    # >>> {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
    #     {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}

    contact = create_contact("Laura Neri", email="laura.neri@domain.com")
    print(create_contact("Laura Neri", email="laura.neri@domain.com"))
    print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))
    # >>> {'profile': 'Laura Neri', 'email': 'laura.neri@domain.com', 'telefono': None}
    # {'profile': 'Laura Neri', 'email': 'laura.new@domain.com', 'telefono': 84736736}