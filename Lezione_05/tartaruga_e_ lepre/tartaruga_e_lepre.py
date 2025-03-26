from random import randint

def random_hare() -> int:
    i = randint(1, 10)
    match i:
        #Riposo
        case 1|2:
            return 0
        
        #Grande balzo
        case 3|4:
            return 9
        
        #Grande scivolata
        case 5:
            return -12
        
        #Piccolo balzo
        case 6|7|8:
            return 1
        
        #Piccola scivolata
        case _:
            return -2
            

def random_turtle() -> int:
    i = randint(1, 10)

    #Passo veloce
    if i >= 1 and i <= 5:
        return 3
    
    #Scivolata
    elif i >= 6 and i <= 7:
        return -6
    
    #Passo lento
    else:
        return 1

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

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while square["Hare"] < 70 and square["Turtle"] < 70:

    #Make them move (randomly)
    square["Hare"] += random_hare()
    square["Turtle"] += random_turtle()

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