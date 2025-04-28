from formagenerica import GenericShape

class Rectangle(GenericShape):

    # Initialize an object of the class Rectangle

    def __init__(self):
        super().__init__()

        self.setShape("rectangle")
    
    def draw(self) -> None:
        print(f"\n{self.getShape()}")

        # Outer for
        for i in range(5):
            # Inner for
            for j in range(5*2):

                # Side a and Side d of the rectangle
                if i == 0 or i == 5-1:
                    print("*", end="  ")
                
                # Side b and Side c of the rectangle
                elif j == 0 or j == 5*2-1:
                    print("*", end="  ")
                
                # White spaces
                else:
                    print(" ", end= "  ")
            print("\n")