'''Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
'''

class Account:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance: float = 0

    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = dict()

    def create_account(self, account_id) -> None:
        if account_id not in self.accounts.keys():
            self.accounts[account_id] = Account(account_id)
        else:
            print("Account with this ID already exists")
        
        return self.accounts[account_id]
    
    def deposit(self, account_id, amount) -> None:
        if account_id in self.accounts.keys():
            if amount >= 0:
                self.accounts[account_id].deposit(amount)
            else:
                print("Err deposit 2")
        else:
            print("Err deposit 1")

    def get_balance(self, account_id) -> None:
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()
        else:
            raise ValueError("Account not found")