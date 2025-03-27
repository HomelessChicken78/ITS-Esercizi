from random import randint

def hare_movement(init_posit: int, raining: bool, stamina: int) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0
    if raining:
        weather_modifier = 2

    #Randomly pick a movement
    match i:
        #Riposo
        case 1|2:
            return init_posit, stamina + 10

        #Grande balzo
        case 3|4:
            if stamina >= 15:
                return init_posit + 9 - weather_modifier, stamina - 15
        
        #Grande scivolata
        case 5:
            if stamina >= 20:
                return init_posit - 12 - weather_modifier, stamina - 20
        
        #Piccolo balzo
        case 6|7|8:
            if stamina >= 5:
                return init_posit + 1 - weather_modifier, stamina - 5
        
        #Piccola scivolata
        case _:
            if stamina >= 8:
                return init_posit -2 - weather_modifier, stamina - 8
    return init_posit, stamina  #In case the picked movement cannot be done due to stamina
            

def turtle_movement(init_posit: int, raining: bool, stamina: int) -> int:
    i = randint(1, 10)
    weather_modifier: int = 0

    if raining:
        weather_modifier = 1

    #Randomly pick a movement
    #Passo veloce
    if i >= 1 and i <= 5:
        if stamina >= 5:
            return init_posit + 3 - weather_modifier, stamina - 5
    
    #Scivolata
    elif i >= 6 and i <= 7:
        if stamina >= 10:
            return init_posit - 6 - weather_modifier, stamina - 10
    
    #Passo lento
    elif stamina >= 3:
        return init_posit + 1 - weather_modifier, stamina - 3
    
    return init_posit, stamina + 10  #In case the picked movement cannot be done due to stamina

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

#Obstacles scattered around the map
obstacles: dict[int, int] = {
    5 : 1, 10 : 1,
    17 : 2, 29 : 1,
    33 : 1, 37 : 2,
    48 : 3, 51 : 1,
    52 : 2, 60 : 3,
    67 : 2, 69 : 9,
    81 : 5, 84 : 2,
    90 : 3, 95 : 2
}

#Bonus scattered around the map
bonus: dict[int, int] = {
    12 : 1, 18 : 1,
    25 : 3, 36 : 2,
    50 : 9, 57 : 2,
    64 : 3, 71 : 2,
    79 : 2, 88 : 3,
    94 : 1, 98 : 1
}

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
    square["Hare"], stamina["Hare"] = hare_movement(square["Hare"], raining, stamina["Hare"])
    square["Turtle"], stamina["Turtle"] = turtle_movement(square["Turtle"], raining, stamina["Turtle"])

    #If they end up on an obstacle, make sure the obstacle does their job
    if square["Hare"] in obstacles:
        square["Hare"] -= obstacles[square["Hare"]]
    if square["Turtle"] in obstacles:
        square["Turtle"] -= obstacles[square["Turtle"]]

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