class ContactManager:
    def __init__(self):
        self._contacts: dict[str, list[str]] = {} # {"Giacomo" : ["132687423", "+39 23178647", "+39 777 936 6483"], "Liam" : ["+39 747 933 102", "+49 123 445 6012"]}

    def create_contact(self, name: str, phone_numbers: list[str]) -> str|dict[str, list[str]]:
        '''Crea un nuovo contatto,
        aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri
        di telefono.\n Restituisce un nuovo dizionario con il solo contatto appena creato o il
        messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.'''
        name = name.title()
        if name in self._contacts:
            return "Errore: il contatto esiste già."
        self._contacts[name] = phone_numbers
        return {name : self.list_phone_numbers(name)}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> str|dict[str, list[str]]:
        '''Aggiunge un numero di telefono al contatto specificato.\n
        Restituisce un nuovo dizionario con il solo contatto aggiornato
        o i messaggi di errore "Errore: il contatto non esiste."
        se il contatto non esiste oppure "Errore: il numero di telefono esiste già."
        se il numero di telefono è già presente per il contatto specificato.
        '''
        contact_name = contact_name.title()
        if contact_name not in self._contacts:
            return "Errore: il contatto non esiste."
        elif phone_number in self._contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        else:
            self._contacts[contact_name].append(phone_number)
            return {contact_name : self.list_phone_numbers(contact_name)}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> str|dict[str, list[str]]:
        '''Rimuove un numero di telefono dal contatto specificato.\n
        Restituisce un nuovo dizionario con il solo contatto aggiornato
        o i messaggi di errore "Errore: il contatto non esiste." se
        il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il
        numero di telefono non esiste per il contatto specificato.'''

        contact_name = contact_name.title()
        if contact_name not in self._contacts:
            return "Errore: il contatto non esiste."
        elif phone_number not in self._contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        else:
            self._contacts[contact_name].remove(phone_number)
            return {contact_name : self.list_phone_numbers(contact_name)}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        '''Sostituisce un numero di telefono con un altro nel
        contatto specificato.\nRestituisce un nuovo dizionario con il solo contatto
        aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non
        esiste oppure "Errore: il numero di telefono non è presente." se il numero di
        telefono non esiste per il contatto specificato.'''
        contact_name = contact_name.title()
        if contact_name not in self._contacts:
            return "Errore: il contatto non esiste."
        elif old_phone_number not in self._contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        else:
            return {contact_name : self.list_phone_numbers(contact_name)}

    def list_contacts(self) -> list[str]:
        '''Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.'''
        return [name for name in self._contacts]

    def list_phone_numbers(self, contact_name: str):
        '''Mostra i numeri di telefono di un
        contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di
        errore "Errore: il contatto non esiste." se il contatto non esiste.'''
        contact_name = contact_name.title()
        if contact_name in self._contacts:
            return self._contacts[contact_name]
        return "Errore: il contatto non esiste."
    
    def search_contact_by_phone_number(self, phone_number: str) -> str|list[str]: 
        '''Trova e restituisce tutti i
        contatti che contengono un determinato numero di telefono.\n Restituisce una lista
        di tutte le chiavi  [self._contacts.keys(MA SOLO QUELLI CON NUMERO SPECIFICATO)] all'interno del dizionario contacts che hanno il numero
        specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con
        questo numero di telefono." se nessun contatto contiene il numero di telefono.'''
        res = []
        for name, numbers in self._contacts.items():
            if phone_number in numbers:
                res.append(name)
        return res if res else "Nessun contatto trovato con questo numero di telefono."