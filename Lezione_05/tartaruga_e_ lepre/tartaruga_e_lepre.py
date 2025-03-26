from random import randint

def hare_movement(raining: bool) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0

    if raining:
        weather_modifier = 2


    match i:
        #Riposo
        case 1|2:
            return 0
        
        #Grande balzo
        case 3|4:
            return 9 - weather_modifier
        
        #Grande scivolata
        case 5:
            return -12 - weather_modifier
        
        #Piccolo balzo
        case 6|7|8:
            return 1 - weather_modifier
        
        #Piccola scivolata
        case _:
            return -2 - weather_modifier
            

def turtle_movement(raining: bool) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0

    if raining:
        weather_modifier = 1

    #Passo veloce
    if i >= 1 and i <= 5:
        return 3 - weather_modifier
    
    #Scivolata
    elif i >= 6 and i <= 7:
        return -6 - weather_modifier
    
    #Passo lento
    else:
        return 1 - weather_modifier

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
    square["Hare"] += hare_movement(raining)
    square["Turtle"] += turtle_movement(raining)

    #Prevent the hare to go behind the start
    if square["Hare"] < 1:
        square["Hare"] = 1

    #Prevent the turtle to go behind the start
    if square["Turtle"] < 1:
        square["Turtle"] = 1

    path = calculate_path(square["Turtle"], square["Hare"])
    print("".join(path))

    if square["Turtle"] >= 70:
        print("TORTOISE WINS! || VAY!!!")
    elif square["Hare"] >= 70:
        print("HARE WINS || YUCH!!!")

    tick += 1