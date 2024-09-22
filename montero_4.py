def mainMenu():

    
    
    print("-- Main Menu --")
    print("[1] - New Transaction")
    print("[2] - Enter Discount Code")
    print("[3] - Calculate Total and Print Receipt")

    userChoice = int(input("Select an option: "))

    return userChoice

def  newTransaction(orderTotal):

    print("[1] - Latte @70.00")
    print("[2] - Americano @55.00")
    print("[3] - Espresso @60.00")
    print("[0] - Back to main menu")

    while True:

        userOrder = int(input("Enter your order: "))
        
        if userOrder == 1:

            orderTotal = orderTotal + 70
            print("Added Latte @70.00")
        
        elif userOrder == 2:

            orderTotal = orderTotal + 55
            print("Added Americano @55.00")

        elif userOrder == 3:

            orderTotal = orderTotal + 60
            print("Added Espresso @60.00")
        
        elif userOrder == 0:
            break

    return orderTotal

def discountCoupon(orderTotal):

    if discountCode ==  "PAYDAY15":

        discount = orderTotal * 0.15
        orderTotal = orderTotal - discount
    
    elif discountCode == "PICKUP10":

        discount = orderTotal * 0.10
        orderTotal = orderTotal - discount

    return orderTotal

def receipt(userName, orderTotal, discountValue):

    while True:
        cash = int(input("Enter cash: "))
        change =  cash - orderTotal

        if cash < orderTotal:
            print("Insufficient Amount!")
        
        else:
            print("Username: ", userName)
            print("Amount Due: ", float(orderTotal))
            print("Cash: ", float(cash))
            print("Change: ", float(change))
            print("Discount: ", str(discountValue) + "%")
            break

# Main Function
userName = input("Enter username: ")
discountValue = 0
orderTotal = 0

while True:

    userChoice = None
    userChoice = mainMenu()

    if userChoice == 1:

        orderTotal = newTransaction(orderTotal)
        print("Your current amount due is", float(orderTotal))
        
    
    elif userChoice == 2:

        while True: 
            discountCode = input("Enter a discount/coupon code: ")

            if discountCode == "PAYDAY15":

                discountValue = 15
                print("Your discount amount is: ", discountValue,"%")
                break

            elif discountCode == "PICKUP10":

                discountValue = 10
                print("Your discount amount is: ", discountValue,"%")
                break
            
            else:
                print("Input a valid code")
            
        orderTotal = discountCoupon(orderTotal)
    
    elif userChoice == 3:

        receipt(userName, orderTotal, discountValue)

    else:
        print("Invalid choice")




       
