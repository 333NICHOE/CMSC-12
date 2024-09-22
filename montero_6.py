# FUNCTION FOR THE MAIN MENU
def mainMenu():
    print("---------- MAIN MENU ----------")
    print("[1] - ADD A PRODUCT")
    print("[2] - VIEW ALL PRODUCTS")
    print("[3] - DELETE A PRODUCT")
    print("[4] - DELETE ALL PRODUCTS")
    print("[5] - RESTOCK A PRODUCT")
    print("[6] - CONSUME A PRODUCT")
    print("[0] - EXIT")

# FUNCTION FOR ADDING THE PRODUCT
def addProduct(inventory):
    
    # LIST THAT WILL CONTAIN THE PRODUCTS
    productList = []

    print("---------- ADD PRODUCT ----------")
    
    prodID = input("ENTER PRODUCT ID: ")

    prodName = input("ENTER PRODUCT NAME: ")
    prodName.append(productList)

    prodDesc = input("ENTER PRODUCT DESCRIPTION: ")
    prodDesc.append(productList)

    prodQuantity = int(input("ENTER PRODUCT QUANTITY: "))
    prodQuantity.append(productList)

    inventory[prodID] = productList

    return inventory

# FUNCTION FOR VIEWING THE PRODUCTS
def viewProducts(inventory):

    print("---------- VIEW PRODUCTS ----------")

    for key, value in inventory.items():
        print(str(key))
        print("NAME: " + str(value[0]))
        print("DESCRIPTION: " + str(value[1]))
        print("QUANTITY: " + str(value[2]))
        print("------------------------------------")

# FUNCTION FOR DELETING A PRODUCT
def deleteProduct(inventory, prodID):
        
    if not prodID in inventory:
        print()







# MAIN FUNCTION

# DICTIONARY THAT WILL CONTAIN THE VALUES OF THE INVENTORY
inventory = {}

while True:

    # CALLS THE FUNCTION THAT WILL DISPLAY THE MENU
    mainMenu()

    # ASKS THE USER FOR THE CHOICE
    mainMenuChoice = int(input("ENTER CHOICE: "))

    # ADDING A PRODUCT
    if mainMenuChoice == 1:
        inventory = addProduct(inventory)
    
    elif mainMenuChoice == 2:
        viewProducts(inventory)

    elif mainMenuChoice == 3:
        print("delete a product")
        productID = input("ENTER PRODUCT ID: ")
        inventory = deleteProduct(inventory, productID)
    # EXIT
    elif mainMenuChoice == 0:
        print("THANK YOU FOR USING MY PROGRAM!")
        break
    else:
        print("INVALID CHOICE! TRY AGAIN!")



