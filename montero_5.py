# FUNCTION FOR THE MAIN MENU
def mainMenu():
    print("[1] - Enter List of Text/s")
    print("[2] - Encrypt")
    print("[3] - View Encrypted")
    print("[4] - Exit")

# FUNCTION FOR GETTING THE TEXT LIST
def getTextList():

    # LIST FOR THE TEXT WHERE THE MESSAGE WOULD BE APPENDED TO
    textList = []

    # ASKS FOR THE USER ON HOW MANY TEXT THEY WOULD LIKE TO ADD
    option = int(input("How many text would you like to add? "))

    
    # ITERATE OVER THE OPTION -> WILL CONTINUOUSLY ASK THE USER FOR INPUT UNTIL IT REACHES THE VALUE FOR OPTION
    for i in range(option):

        while True:
            # ASKS FOR THE TEXT INPUT -> AUTOMATICALLY SETS THE TEXT TO LOWERCASE
            message = input("Enter text" + "[" + str(i+1) + "]: ").lower()

            # CHECKS IF THE INPUT IS BLANK -> IF YES, ASKS AGAIN
            if not message:
                print("You can't leave this blank")
            
            # ADDS THE MESSAGE IN THE 'textList'
            else:
                textList.append(message)
                break
            

    return textList

# FUNCTION FOR COMPRESSING THE TEXT
def compress(text):

    # VARIABLE WHERE THE VALUE OF THE COMPRESSED TEXT WOULD BE PLACES
    compressedText = ""

    # COUNTER FOR THE NUMBER OF CONSECUTIVE LETTERS
    occurrences = 1 

    # ITERATE OVER THE LENGTH OF THE TEXT
    for i in range(1, len(text)):

        # CURRENT CHARACTER TRACKER
        current_char = text[i]

        # PREVIOUS CHARACTER TRACKER
        prev_char = text[i - 1]

        # IF THE CURRENT CHAR IS THE SAME AS THE PREV CHAR -> INCREMENT OCCURENCES
        if current_char.lower() == prev_char.lower():
            occurrences += 1
        
        # WHEN CURRENT IS DIFFERENT FROM PREV CHAR
        else:
            
            # IF THERE IS MORE THAN 1 OCCURNCE -> APPEND THE LETTER FOLLOWED BY THE COUNT
            if occurrences > 1:
                compressedText += prev_char + str(occurrences)

            # WHEN THERE IS ONLY ONE OCCURENCE -> APPEND THE LETTER W/O A COUNT
            else:
                compressedText += prev_char

            # RESETTING THE THE OCCURENCE FOR ANOTHER ITERATION
            occurrences = 1 

    # HANDLING THE LAST CHARACTER
    if occurrences > 1:
        compressedText += current_char + str(occurrences)
    else:
        compressedText += current_char

    return compressedText

# FUNCTION FOR THE ENCRYPTION ALGORITHM
def encrypt(textList, shift):

    # LIST THAT WILL CONTAIN THE ENCRYPTED TEXT
    encryptedList = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # ITERATE OVER THE 'textList' FOR EVERY TEXT
    for text in textList:
        # VARIABLE THAT WILL CONTAIN THE CURRENT TEXT 
        caesarCipherText = ""
        # ITERATE OVER TEXT FOR EVERY CHAR
        for char in text:
            if char in alphabet:
                # GETS THE POSTION/INDEX OF 'char'
                pos = alphabet.index(char.lower())

                # GETS THE NEW POSITION BY ADDING THE NUMBER OF SHIFTS
                newPos = (pos + shift) % 26

                # THE NEW ENCRYPTED MESSAGE IS OBTAINED by using the 'newPos' as index in the alphabet
                caesarCipherText += alphabet[newPos] if char.islower() else alphabet[newPos].upper()
            else: 
                caesarCipherText += char

        # COMPRESS FUNCTION THAT WILL COUNT THE OCCURENCES OF CONSECUTIVE CHAR
        compressedText = compress(caesarCipherText)

        # APPENDS THE COMPRESSED TEXT TO THE ENCRYPTED LIST
        encryptedList.append(compressedText)

    return encryptedList


# FUNCTION FOR VIEWING THE ENCRYPTED TEXT/S
def view_encrypted(originalList, encryptedList):
    
    if len(originalList) != len(encryptedList):
        print("LIST MUST BE THE SAME LENGTH!")
        return

    for i in range(len(originalList)):
        print("Original: " + originalList[i] + "-----> Encrypted: " + encryptedList[i])

# MAIN FUNCTION
originalText = []
shift = 0

while True:
    mainMenu()
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("THIS IS OPTION 1")
        originalText = getTextList()

    elif choice == 2:
        print("THIS IS OPTION 2")
        shift = int(input("Enter number of shifts: "))
        encryptedList = encrypt(originalText, shift)

    elif choice == 3:
        print("THIS IS OPTION 3")
        if originalText and encryptedList:
            view_encrypted(originalText, encryptedList)
        else:
            print("No ciphers yet, enter words and encrypt them.")

    elif choice == 4:
        print("THANK YOU FOR USING MY PROGRAM!")
        break
    else:
        print("Invalid Choice")
    