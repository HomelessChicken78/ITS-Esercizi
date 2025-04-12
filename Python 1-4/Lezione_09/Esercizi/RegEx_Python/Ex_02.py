'''

2. Trova tutte le email in un testo

Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

Esempio:

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']
'''

from re import findall

def find_emails(email: str) -> list[str]:
    '''Returns a list containing all the emails found in a string'''
    return [mail.lower() for mail in findall(r"[a-zA-Z][a-zA-Z0-9_\.]+@[a-zA-Z]\w+\.[a-zA-Z0-9_\.]+", email)]

#Expected Output
if __name__ == "__main__":
    print(find_emails("bla bla bla email@provider.dominio bla bla bla"))  #['email@provider.dominio']
    print(find_emails("Contattaci a info@azienda.com oppure support@help.org"))  #['info@azienda.com', 'support@help.org']
    print(find_emails("Cristiano.Coccia@its.ict.academy.2025"))  #email.email@provider.dominio.dominio