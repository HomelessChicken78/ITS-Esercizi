'''3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''

#Initialize the product stock
def products(**kwargs) -> dict[str, list[float, int]]:
    products: dict[str, list[float, int]] = {}
    for k, v in kwargs.items():
        products[k] = v
    return products

products_stock: dict[str, list[float, int]] = products(
    milk = [1.5, 30],
    pasta = [1.0, 50],
    flour = [0.5, 10],
    sugar = [0.5, 7],
    tomato_sause = [1.0, 20],
    olive_oil = [20.0, 7],
    biscuits = [3.2, 17],
    legumes = [0.2, 38],
    tuna = [0.4, 22]
)


#This function add new products to the cart
def add_to_cart(cart: dict[str, list[float, int]], product_stock: dict[str, list[float, int]], new_product: str, quantity: int = 1):
    if product_stock[new_product][1] >= quantity:  #Check if the product is out of stock

        #If the item is already in the cart just increase its quantity by one
        if new_product in cart:
            cart[new_product][1] += quantity

        #If the item has never been added to the cart before, add it to the cart
        else:
            cart[new_product] = [product_stock[new_product][0], quantity]
        
        print("Product added to cart!")

    else:
        print("\nWARNING: The product is out of stock or the asked quantity exceed the stock\n")
    return cart

#This function remove products from the cart
#This function adds products to the stock
#This function remove products from the stock
def remove_from_stock(product_stock: dict[str, list[float, int]], removed_product: str, quantity: int = 1) -> dict[str, list[float, int]]:    
    if removed_product in product_stock:
        product_stock[removed_product][1] -= quantity if product_stock[removed_product][1] >= quantity else 0
    return product_stock


#This function allow a clean view of the cart's products
def view_cart(cart: dict[str, list[float, int]]):
    if cart:
        print(f"Your cart is:")
        for name, lst in cart.items():
            print(f"--------------------\n{name.title()}: ")
            print(f"Price: {lst[0]:.2f}€,\nQuantity: {lst[1]}")

    else:
        print("Your cart is empty!")


#Define variables for the user's command prompts
action: str = ""
primary_action: str = ""
secondary_action: str = ""
tertiary_action: str = ""

cart: dict[str, float] = {}
while action != "finish" and action != "pay":
    print("Here you can manage your shopping cart. For a list of commands type \"help\"")
    action = input("->\t").lower()
    secondary_action = ""
    tertiary_action = ""

    #Split the string "action" into sub-commands using the function split
    if len(action.split()) >= 1:
        primary_action = action.split()[0]
    if len(action.split()) >= 2:
        secondary_action = action.split()[1].lower()
    if len(action.split()) >= 3:
        tertiary_action = action.split()[2].lower()

    match primary_action:

        #In case the user types "helps"
        case "help":
            print('''List of commands:
                  "help": provide the list of commands,
                  "add <product> [amount]": add a product to the cart,
                  "remove <product> [amount]": remove a product from the cart
                  "finish" or "pay" to end the program''')

        #If the user types "add"
        case "add":
            #Check if typed product is in the stock
            if secondary_action in products_stock:
                tertiary_action = "1" if not tertiary_action else tertiary_action  #If the user has not typed the quantity, bring the quantity automatically to 1
                
                #Check if the user has typed tertiary action is a number
                if tertiary_action.isnumeric():
                    tertiary_action = int(tertiary_action)
                else:
                    print("\nWARNING: You did not type a number for the quantity\n")
                    continue
                cart = add_to_cart(cart, products_stock, secondary_action, tertiary_action)
                products_stock = remove_from_stock(products_stock, secondary_action, tertiary_action)

            #If not, check if the user has even typed something. If it did not type anything, it means they forgot. Ask the user to type the secondary action
            elif secondary_action == "":

                #Print out the product's stock
                for prod, infos in products_stock.items():
                    print(f"{prod}:\n", end="")
                    for info in infos:
                        if info == infos[0]:
                            print(f"Cost: {info:.2f}€ | ", end="")
                        else:
                            print(f"Quantity: {info}\n")

                action = "add " + input("add ").lower()
                if len(action.split()) >= 2:
                    secondary_action = action.split()[1].lower()
                if len(action.split()) >= 3:
                    tertiary_action = action.split()[2].lower()

                if secondary_action in products_stock:
                    tertiary_action = "1" if not tertiary_action else tertiary_action  #If the user has not typed the quantity, bring the quantity automatically to 1
                    
                    #Check if the user has typed tertiary action is a number
                    if tertiary_action.isnumeric():
                        tertiary_action = int(tertiary_action)
                    else:
                        print("\nWARNING: You did not type a number for the quantity\n")
                        continue
                    cart = add_to_cart(cart, products_stock, secondary_action, tertiary_action)
                    products_stock = remove_from_stock(products_stock, secondary_action, tertiary_action)


                elif secondary_action == "":
                    print("\nWARNING: You did not specify what product you want to add!\n")
                    continue
                
                else:
                    print("\n -- WARNING: The product does not exist. Type \"add\" without any argument to see the stock list --\n")


            #Finally, if the user typed something, but the product does not exist in the market, it means they are searching for an unexistant item. Print a warning
            else:
                print("\n -- WARNING: The product does not exist. Type \"add\" without any argument to see the stock list --\n")

        case "remove":
            print("WIP")

        case "view":
            view_cart(cart)
        
        case "finish"|"pay":
            pass


        #If the command does not exist, print a warning
        case _:
            print("\nWARNING: The typed command does not exist. Type \"help\" for a list of commands.\n")

view_cart(cart)