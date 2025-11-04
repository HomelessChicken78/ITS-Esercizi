'''Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare,
modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di
gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una
    lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un
    messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata.
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata.
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente
    con un altro nella ricetta specificata.
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta.
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.'''

class RecipeManager:
    def __init__(self):
        self.recipes: dict[str, list[str]] = dict()

    def create_recipe(self, recipe_name: str, ingredients: list[str]) -> dict[str, list[str]]|str:
        if recipe_name not in self.recipes.keys():
            self.recipes[recipe_name] = ingredients
            return {recipe_name : self.recipes[recipe_name]}
        else:
            return "Err create recipe 1"
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]|str:
        if recipe_name in self.recipes.keys():
            if ingredient not in self.recipes[recipe_name]:
                self.recipes[recipe_name].append(ingredient)
                return {recipe_name : self.recipes[recipe_name]}
            else:
                return "Err add ingr 2"
        else:
            return "Err add ingr 1"
    
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]|str:
        if recipe_name in self.recipes.keys():
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return {recipe_name : self.recipes[recipe_name]}
            else:
                return "Err rem ingr 2"
        else:
            return "Err rem ingr 1"
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]|str:
        if recipe_name in self.recipes.keys():
            if old_ingredient in self.recipes[recipe_name]:
                # i guess the new recipe has to be added at the end. otherwise i can use an insert with a .index - yes., i have to
                index =self.recipes[recipe_name].index(old_ingredient)
                self.recipes[recipe_name].remove(old_ingredient)
                self.recipes[recipe_name].insert(index, new_ingredient)
                return {recipe_name : self.recipes[recipe_name]}
            else:
                return "Err upd ingr 2"
        else:
            return "Err upd ingr 1"
    
    def list_recipes(self) -> list[str]:
        res: list[str] = []

        for recipe in self.recipes.keys():
            res.append(recipe)

        return res

    def list_ingredients(self, recipe_name) -> list[str]|str:
        if recipe_name not in self.recipes.keys():
            return "Err list ingr 1"

        res: list[str] = []

        for element in self.recipes[recipe_name]:
            res.append(element)
        
        return res

    def search_recipe_by_ingredient(self, ingredient: str) -> list[str]:
        res: dict[str, list[str]] = dict()

        for recipe, ingredients in self.recipes.items():
            if ingredient in ingredients:
                res[recipe] = ingredients
        
        return res if res else "err search ingr 1"
    
 	

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
 	

        
'''- list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta.
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.'''