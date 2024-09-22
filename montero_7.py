def mainMenu():

    print("----------------------MENU----------------------")
    print("[1] - Add a Product")
    print("[2] - View Products")
    print("[3] - Delete a Product")
    print("[4] - Delete All Products")
    print("[5] - Restock a Product")
    print("[6] - Consume a Product")
    print("[7] - Load")
    print("[8] - Save")
    print("[0] - Exit")

def addProduct(inventory):

    productList = []
    print("----------------------ADD PRODUCT----------------------")
    prodID = input("Enter Product ID: ")
    prodName = input("Enter Product Name: ")
    productList.append(prodName)
    prodDesc = input("Enter Product Description: ")
    productList.append(prodDesc)
    prodQuantity = int(input("Enter Product Quantity: "))
    productList.append(prodQuantity)

    inventory[prodID] = productList

    return inventory

def viewProducts(inventory):

    print("----------------------VIEW PRODUCTS----------------------")
    for key, value in inventory.items():
        print(str(key))
        print("Name: ", str(value[0]))
        print("Description: ", str(value[1]))
        print("Quantity: ", value[2])
        print("---------------------------------------------------------")

def deleteProduct(inventory, prodID):
     
    if not prodID in inventory:
        print("ID is invalid")
    else:
        del inventory[prodID]
    
    return inventory

def deleteAll(inventory):

    inventory.clear()
    return inventory


def restockProduct (inventory, prodID):
    if not prodID in inventory:
        print("ID is invalid")
    else: 
        restockProd = int(input("Enter how many you would like to restock: "))
        inventory[prodID][2] = restockProd + inventory[prodID][2]

def consumeProduct (inventory, prodID):
    if not prodID in inventory:
        print("ID is invalid")
    else: 
        consumeProd = int(input("Enter amount to consume: "))
        if inventory[prodID][2] < consumeProd:
            print("Not enough products")
        else:
            inventory[prodID][2] = inventory[prodID][2] - consumeProd
            print("Consumed " + str(consumeProd) + " of " + inventory[prodID][0])


def loadInventory (inventory): #accepts a dictionary, that performs a load operation on a file called inventory.dat
	fh = open("inventory.dat", "r")
	for line in fh:
		line = line.split(",")
		inventory[line [0]] = [line[1],line[2], int(line[3])] 
	fh.close()
	print("inventory.dat successfully loaded")
	

def saveInventory (inventory):  #accepts a dictionary, that performs a save operation of your inventory on a file called inventory.dat.
	fh = open("inventory.dat", "w")
	for key, value in inventory.items(): 
		fh.write(str(key) +","+ value[0] +","+ value[1] +","+ str(value[2]) + "," + "\n")
	fh.close()
	print("inventory.dat successfully saved")


		
	
#Main
inventory = {}
while True:
    mainMenu()
    mainMenuChoice = int(input("SELECT AN OPTION: "))

    if mainMenuChoice == 0:
        break
    
    elif mainMenuChoice == 1:

        inventory = addProduct(inventory)
        
    
    elif mainMenuChoice == 2:

        viewProducts(inventory)
    
    elif mainMenuChoice == 3:

        productId = input("ENTER ID TO DELETE: ")
        inventory = deleteProduct(inventory, productId)

    elif mainMenuChoice == 4:

        if len(inventory) == 0:
            print("No items to delete")
            continue

        else:
            inventory = deleteAll(inventory)
            
    elif mainMenuChoice == 5:
        productId = input("Enter product ID: ")
        restockProduct (inventory, productId)
        
    elif mainMenuChoice == 6:
        productId = input("Enter product ID: ")
        consumeProduct (inventory, productId)
        
    elif mainMenuChoice == 7:
         productList = loadInventory(inventory)
         
    elif mainMenuChoice == 8:
         saveInventory(inventory)
        
    elif mainMenuChoice == 0:
        print("invalid choice")
        break






