class RecipeManager:
    def __init__(self):
        self.recipe_list: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> None:
        '''Crea una nuova ricetta con il nome specificato e una
        lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un
        messaggio di errore se la ricetta esiste già.'''

        if name not in self.recipe_list:
            self.recipe_list[name] = ingredients
            return {name : ingredients}
        else:
            return f"Una ricetta nominata \"{name}\" già esiste!"
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> None:
        '''Aggiunge un ingrediente alla ricetta specificata.\n
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste
        già o la ricetta non esiste.'''
        if recipe_name not in self.recipe_list:
            return f"Non esiste alcuna ricetta di nome \"{recipe_name}\"!"
        elif ingredient in self.recipe_list[recipe_name]:
            return f"L'ingrediente \"{ingredient}\" è già presente nella ricetta \"{recipe_name}\""
        else:
            self.recipe_list[recipe_name].append(ingredient)
            return {recipe_name : self.recipe_list[recipe_name]}
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        '''Rimuove un ingrediente dalla ricetta specificata.
        \nRestituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è
        presente o la ricetta non esiste.'''
        if recipe_name not in self.recipe_list:
            return f"Non esiste alcuna ricetta di nome \"{recipe_name}\"!"
        elif ingredient not in self.recipe_list[recipe_name]:
            return f"L'ingrediente \"{ingredient}\" non è presente nella ricetta \"{recipe_name}\""
        else:
            self.recipe_list[recipe_name].remove(ingredient)
            return {recipe_name : self.recipe_list[recipe_name]}
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        '''Sostituisce un ingrediente con un altro nella ricetta specificata.\n
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è
        presente o la ricetta non esiste.'''
        if recipe_name not in self.recipe_list:
            return f"Non esiste alcuna ricetta di nome \"{recipe_name}\"!"
        elif old_ingredient not in self.recipe_list[recipe_name]:
            return f"L'ingrediente \"{old_ingredient}\" non è presente nella ricetta \"{recipe_name}\""
        else:
            self.recipe_list[recipe_name].insert(self.recipe_list[recipe_name].index(old_ingredient), new_ingredient)
            self.recipe_list[recipe_name].remove(old_ingredient)
            return {recipe_name : self.recipe_list[recipe_name]}
    
    def list_recipes(self) -> list[str]:
        '''Elenca tutte le ricette esistenti.'''
        return [k for k in self.recipe_list.keys()]
    
    def list_ingredients(self, recipe_name) -> list[str]:
        '''Mostra gli ingredienti di una specifica ricetta.\n
        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.'''
        if recipe_name not in self.recipe_list:
            return f"Non esiste alcuna ricetta di nome \"{recipe_name}\"!"
        else:
            return self.recipe_list[recipe_name]

    def search_recipe_by_ingredient(self, ingredient): 
        '''Trova e restituisce tutte le ricette che contengono un determinato ingrediente.\n
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta
        contiene l'ingrediente.'''
        recipes: list[str] = self.list_recipes()
        result: list[str] = {}

        for r in recipes:
            for i in self.recipe_list[r]:
                if i == ingredient:
                    result[r] = self.recipe_list[r]
        return result


if __name__ == "__main__":
    RM: RecipeManager = RecipeManager()
    print(RM.create_recipe("ciao", ["bontà", "gentilezza", "educazione"]))
    print(RM.create_recipe("ciao", []))
    print(RM.add_ingredient("THIS RECIPE DOESN'T EXIST", "NO"))
    print(RM.add_ingredient("ciao", "bontà"))
    print(RM.recipe_list)
    RM.add_ingredient("ciao", "Mozzarella di Bufala")
    print("\n\n")



    manager = RecipeManager()
    print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
    print(manager.add_ingredient("Pizza Margherita", "Basilico"))
    print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
    print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
    print(manager.list_recipes())
    print(manager.list_ingredients("Pizza Margherita"))
    print(manager.search_recipe_by_ingredient("Mozzarella di Bufala"))