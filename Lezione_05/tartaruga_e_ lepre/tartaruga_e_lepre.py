from random import randint

def hare_movement(raining: bool, stamina: int) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0
    if raining:
        weather_modifier = 2

    #Randomly pick a movement
    match i:
        #Riposo
        case 1|2:
            return 0, stamina + 10

        #Grande balzo
        case 3|4:
            if stamina >= 15:
                return 9 - weather_modifier, stamina - 15
        
        #Grande scivolata
        case 5:
            if stamina >= 20:
                return -12 - weather_modifier, stamina - 20
        
        #Piccolo balzo
        case 6|7|8:
            if stamina >= 5:
                return 1 - weather_modifier, stamina - 5
        
        #Piccola scivolata
        case _:
            if stamina >= 8:
                return -2 - weather_modifier, stamina - 8
    return 0, stamina  #In case the picked movement cannot be done due to stamina
            

def turtle_movement(raining: bool, stamina: int) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0

    if raining:
        weather_modifier = 1

    #Randomly pick a movement
    #Passo veloce
    if i >= 1 and i <= 5:
        if stamina >= 5:
            return 3 - weather_modifier, stamina - 5
    
    #Scivolata
    elif i >= 6 and i <= 7:
        if stamina >= 10:
            return -6 - weather_modifier, stamina - 10
    
    #Passo lento
    elif stamina >= 3:
        return 1 - weather_modifier, stamina - 3
    
    return 0, stamina + 10  #In case the picked movement cannot be done due to stamina

def calculate_path(T: int, H: int) -> list[str]:
    path: list[str] = []
    for square in range(1, 70):
        if square == T and square == H:
            path.append("OUCH!!!")
        elif square == T:
            path.append("T")
        elif square == H:
            path.append("H")
        else:
            path.append("_")

    return path

tick: int = 0
square: dict[str, int] = {"Turtle" : 1, "Hare" : 1}  #Starting point for both
stamina: dict[str, int] = {"Turtle" : 100, "Hare" : 100}  #Starting stamina for both
info: tuple[dict[str, int], dict[str, int]] = ()  #Used to return multiple dictionaries from the movement functions
path: list[str] = []
raining: bool = False

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while square["Hare"] < 70 and square["Turtle"] < 70:

    #Weather modifications
    if tick % 10 == 0 and tick != 0:
        if raining:
            raining = False
            #print("\n\n\t\t\tIt's sunny now!!!")
        else:
            raining = True
            #print("\n\n\t\t\tIt started to rain")

    #Make them move (randomly)
    info = hare_movement(raining, stamina["Hare"])
    square["Hare"] += info[0]
    stamina["Hare"] = info[1]
    info = turtle_movement(raining, stamina["Turtle"])
    square["Turtle"] += info[0]
    stamina["Turtle"] = info[1]


    #Prevent the hare to go behind the start
    if square["Hare"] < 1:
        square["Hare"] = 1

    #Prevent the turtle to go behind the start
    if square["Turtle"] < 1:
        square["Turtle"] = 1

    #Prevent the hare from getting more stamina than the cap
    if stamina["Hare"] > 100:
        stamina["Hare"] = 100
    #Prevent the turtle from getting more stamina than the cap
    if stamina["Turtle"] > 100:
        stamina["Turtle"] = 100

    path = calculate_path(square["Turtle"], square["Hare"])
    print("".join(path))

    if square["Turtle"] >= 70:
        print("TORTOISE WINS! || VAY!!!")
    elif square["Hare"] >= 70:
        print("HARE WINS || YUCH!!!")

    tick += 1