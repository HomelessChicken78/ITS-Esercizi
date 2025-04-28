class Alien:
    '''
    For an alien we need to know the provenience galaxy
    self.galaxy: str
    '''

    #Initialize an object of the class Alien
    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            raise ValueError("The galaxy of provenience cannot be represented by an empty string")
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.galaxy}"
    
    def speak(self) -> None:
        print("h̶̡̨̧̢̤̜̟̼͖̪̮̹̤̬̺̥̺͔͍̦̫̫̝̭̪͚͍̻͍̩̤͍̭͂̓̀͗̑̓͋̒͂̾͐̓̈́̉̉́̂̆̔̄̈́̒̇̑͛̐̑͂̀͑̎͂̕͜͝͝͝͝͝͝ͅī̵̢̨̨̢̡̨̢̨̧̨̢̡̛̛̼̜̪͎͕̱̩̖̦̗̣̩͉̝̤͙̥̻̖̭̦̤̮̤̞̻̥̝̱͙̗̰̫̹̝̭̼̖̝̘͉̺̱͓̯̺̤̜̘̮̪͕̣̙̻͚̖͚͙̱̭̼͍̙̟͍̘̠̯̘͇̖̦͇̮̖̺̞̙͈͇̝̣̙̺̪̰̦̖̙̭͔͎̤̭̪̮̳͓͕͉͔͙̺̺̻̭͉̻͕̞̰̞̰͖̲̗̬̖͔̼̭̩̼̲̘͍̮͎̭͎͍̙̣͕̟͉̤͚͖̙͖͇̮̞̹̳̠̩̬̼͇͕̪̣͈̹͈͖͇̞̮̮̺̮̳̘̜͎̞̳̬̬͓͖̺͎̳̜̟̪̜͚̳̟̫̥̼͓̫͓̠̙͈̪̞͓̤͔̟̲̹̪̪̳̗̙̳̙̱̫͍̞̱͇̦̲̰͙͖̜̗͉̞͇̥̣̘̮̭̮͍̣͇̭̹͍̱̜̲͍̜̼̻̖͖̭̘̙͔̪͍͖̪̬͖̩͍͙͎̮̏̀̍̊̅̓͛̓̎̏̒̊̃͑͊̐͗͛̽̒̆̑͊̏̊̅̿̀̊̓̓͒͛̄̑̀̈́̀̍̏̆̀̅̈́̍̈́̂̿̃̈͂͒̀͐̄͆̾͂̈́͑̅̽̏͂̓͂͘̕̕͜͜͜͜͜͝ͅͅͅͅͅͅͅͅͅͅͅư̵̧̨̡̢̧̡̨̡̨̧̨͈̟͎̥̫̣̤̣̙͈̰͓͉̫̹̞̥͖͔̦͔̲͔̞͙̰̙̼͈̟̹͉̱̦̱̼̟̞̻̼̳̺̣͈̼̝͕͉̤̜̱̝̠͓̞̤̦̜̬̻̦̰͈̞͇̯̗̼̞͍̯̭̦͉͔͎̜̭̖̠̭̯͉̹͓̬̭̦̺̣̥̼̮̤̖̱̯̳͓̘̜̣̳̹͇͔͔͉̰͖̭͖̳̗͖̜͈̹͔̪̮̭̳̙̠͎̳͕̲̭͇̰̝̜̱̗̱̰̰͕̮̺͉̳̭̩̭̯͍͑̈́̌̂̽̊̾͋́̓͐͗̍̏́̋̈́̃͛̆͂̉͐̆̋̉̈́̍͆̾͗́̐͛̄̚͘̕̚͘̚͜͜͜͜͜͝͝͠͠ͅͅ")