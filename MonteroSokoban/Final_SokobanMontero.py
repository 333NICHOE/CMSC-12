import platform
import os 
import time

#Array for the time
saveTimeArray1 = []
saveTimeArray2 = []
saveProgressArray = []

#10x10 Save Time Function
def saveTime10(saveTimeArray1):
    fileHandler = open("10x10SavedTime.txt", "a")
    for line in saveTimeArray1:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#10x10 Access Saved File for Time
def readTime10():
    saveTimeArray1 = []
    fileHandler = open("10x10SavedTime.txt", "r")
    for line in fileHandler:
         saveTimeArray1.append(line[:-1])
    fileHandler.close()
    return saveTimeArray1

#15x15 Save Time Function
def saveTime15(saveTimeArray2):
    fileHandler = open("15x15SavedTime.txt", "a")
    for line in saveTimeArray2:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#15x15 Access Saved File for Time
def readTime15():
    saveTimeArray2 = []
    fileHandler = open("15x15SavedTime.txt", "r")
    for line in fileHandler:
         saveTimeArray2.append(line[:-1])
    fileHandler.close()
    return saveTimeArray2

#Saving current progress of game (serves as the function that saves the current time (in seconds) once the saved game is loaded, the time in this file will continue)
#Saving current progress of game
def saveProgress(saveProgressArray):
    fileHandler = open("saveProgress.txt", "a")
    for line in saveProgressArray:
        fileHandler.write(str(line) + "\n")
    fileHandler.close()

#Loading currently saved game (serves as the function that loads the time (in seconds) contained in the saveProgress. Once the saved game is loaded, the time in this file will continue)
#Loading currently saved game
def loadProgress():
    saveProgressArray = []
    fileHandler = open("saveProgress.txt", "r")
    for line in fileHandler:
         saveProgressArray.append(line[:-1])
    fileHandler.close()
    return saveProgressArray

#Saving onto another saved file
def overwriteProgress():
    fileHandler = open("saveProgress.txt", "w")
    fileHandler.write("")
    fileHandler.close() 
    
#put files in a list (allows to access the levels chronologically (after finishing the 1st proceed with the next))
file10 = ["Level1-10x10.txt", "Level2-10x10.txt"]
file15 = ["Level1-15x15.txt", "Level2-15x15.txt"]

#will serve as the index of file10 and file15 (easily get the values in the list)
indexFile = 0


#clears the terminal
def sys_clr():
    if platform.system() == "Windows":
        os.system("cls")
    else: 
        os.system("clear")
        
#10x10 grid level (access)
def loadMap10(indexFile):
    #contains all the list of the lines 
    storeMapList = []

    #stores each line into another list 
    storeMapLineList = []

    fileHandle = open(file10[indexFile], "r")

    for line in fileHandle:
        for item in line[:-1]:
            storeMapLineList.append(item)
        storeMapList.append(storeMapLineList)
        storeMapLineList = []
        
    fileHandle.close()
    return storeMapList

#15x15 grid level (access)
def loadMap15(indexFile):
    
    #contains all the list of the lines  
    storeMapList = []

    #stores each line into another list 
    storeMapLineList = []

    fileHandle = open(file15[indexFile], "r")

    for line in fileHandle:
        for item in line[:-1]:
            storeMapLineList.append(item)
        storeMapList.append(storeMapLineList)
        storeMapLineList = []
        
    fileHandle.close()
    return storeMapList

#access saved map
def loadMapSaved():
    #contains all the list of the lines  
    storeMapList = []

    #stores each line into another list
    storeMapLineList = []

    fileHandle = open("saved.txt", "r")

    for line in fileHandle:
        for item in line[:-1]:
            storeMapLineList.append(item)
        storeMapList.append(storeMapLineList)
        storeMapLineList = []
        
    fileHandle.close()
    return storeMapList

#Printing Maps in the Terminal 
def printSoko2(storeMapList):  
    for mapList in storeMapList[1:]:
        for content in mapList:
            if content == "#":
                print(content, end=" ")
            elif content == "P":
                print(content,end=" ")
            else:
                print(content, end=" ")
        print()

def printSoko(storeMapList):  
    for mapList in storeMapList:
        for content in mapList:
            if content == "#":
                print(content, end=" ")
            elif content == "P":
                print(content, end=" ")
            else:
                print(content, end=" ")
        print()
        
#Function for movement (Moving UP)       
def moveUP(storeMapList):
    for i in range(len(storeMapList)):
        for j in range(len(storeMapList[i])):
            if storeMapList[i][j] == "P":
                if storeMapList[i-1][j] != "#":
                    if storeMapList[i-1][j] == "B":
                        if storeMapList[i-2][j] == "-":
                            storeMapList[i-1][j], storeMapList[i-2][j] = storeMapList[i-2][j], storeMapList[i-1][j] #switches the block (B) in the list with the space(-)
                            storeMapList[i][j], storeMapList[i-1][j] = storeMapList[i-1][j], storeMapList[i][j] #switches the player (P) with the space (-)
                            return storeMapList
                        if storeMapList[i-2][j] == "B": # Player moves a block through another block (the player is not allowed to move the block)
                            return None
                        if storeMapList[i-2][j] == "#": # Player collides with a wall (the player is not allowed to go through a wall)
                            return None
                        if storeMapList[i-2][j] == "D":
                            if storeMapList[i-3][j] != "D":
                                storeMapList[i-2][j] = "X" #block is placed in the correct slot
                                storeMapList[i-1][j] = "-"
                                storeMapList[i][j], storeMapList[i-1][j] = storeMapList[i-1][j], storeMapList[i][j]
                                return storeMapList
                            elif storeMapList[i-3][j] == "D": #is changed here
                                storeMapList[i][j] = "-"
                                storeMapList[i-1][j] = "P"
                                storeMapList[i-2][j] = "X"
                                return storeMapList
                    elif storeMapList[i-1][j] == "-":
                        storeMapList[i][j], storeMapList[i-1][j] = storeMapList[i-1][j], storeMapList[i][j]
                        return storeMapList    
                    elif storeMapList[i-1][j] == "X": #is changed here
                        if storeMapList[i-2][j] != "#":
                            if storeMapList[i-2][j] == "D":
                                storeMapList[i][j] = "-"
                                storeMapList[i-1][j] = "O"
                                storeMapList[i-2][j] = "X"
                                return storeMapList
                if storeMapList[i-1][j] == "D":
                    storeMapList[i-1][j] = "O" # when the player is "on top" of the slot where we put the block (B)
                    storeMapList[i][j] = "-"
                    return storeMapList
                
                if storeMapList[i-1][j] == "X":
                    if storeMapList[i-2][j] != "#":
                        storeMapList[i][j] = "-"
                        storeMapList[i-2][j] = "B"
                        storeMapList[i-1][j] = "O"
                        return storeMapList
                    
            elif storeMapList[i][j] == "O":
                if storeMapList[i-2][j] != "#":
                    if storeMapList[i-1][j] == "B":
                        storeMapList[i-2][j] = "B"
                        storeMapList[i][j] = "D"
                        storeMapList[i-1][j] = "P"
                        return storeMapList
                    elif storeMapList[i-1][j] == "X": #is changed here
                        storeMapList[i][j] = "D"
                        storeMapList[i-1][j] = "O"
                        storeMapList[i-2][j] = "B"
                        return storeMapList
                    else:
                        storeMapList[i][j] = "D"
                        storeMapList[i-1][j] = "P"
                        return storeMapList
                elif storeMapList[i-2][j] == "#":
                    if storeMapList[i-1][j] == "-":
                        storeMapList[i-1][j] = "P"
                        storeMapList[i][j] = "D"
                                                           
def moveDOWN(storeMapList):
    for i in range(len(storeMapList)):
        for j in range(len(storeMapList[i])):
            if storeMapList[i][j] == "P":
                if storeMapList[i+1][j] != "#":
                    if storeMapList[i+1][j] == "B":
                        if storeMapList[i+2][j] == "-":
                            storeMapList[i+1][j], storeMapList[i+2][j] = storeMapList[i+2][j], storeMapList[i+1][j] #switches the block (B) in the list with the space(-)
                            storeMapList[i][j], storeMapList[i+1][j] = storeMapList[i+1][j], storeMapList[i][j] #switches the player (P) with the space (-)
                            return storeMapList
                        if storeMapList[i+2][j] == "B": # Player moves a block through another block (the player is not allowed to move the block)
                            return None
                        if storeMapList[i+2][j] == "#": # Player collides with a wall (the player is not allowed to go through a wall)
                            return None
                        if storeMapList[i+2][j] == "D":
                            if storeMapList[i+3][j] != "D":
                                storeMapList[i+2][j] = "X" #block is placed in the correct slot
                                storeMapList[i+1][j] = "P"
                                storeMapList[i][j] = "-"
                                return storeMapList
                            elif storeMapList[i+3][j] == "D": #is changed here
                                storeMapList[i][j] = "-"
                                storeMapList[i+1][j] = "P"
                                storeMapList[i+2][j] = "X"
                                return storeMapList
                    elif storeMapList[i+1][j] == "-":
                        storeMapList[i][j], storeMapList[i+1][j] = storeMapList[i+1][j], storeMapList[i][j]
                        return storeMapList 
                    elif storeMapList[i+1][j] == "X": #is changed here
                        if storeMapList[i+2][j] != "#":
                            if storeMapList[i+2][j] == "D":
                                storeMapList[i][j] = "-"
                                storeMapList[i+1][j] = "O"
                                storeMapList[i+2][j] = "X"
                                return storeMapList
                            elif storeMapList[i+2][j] == "-":
                                storeMapList[i][j] = "-"
                                storeMapList[i+1][j] = "O"
                                storeMapList[i+2][j] = "B"
                                return storeMapList
                                
                if storeMapList[i+1][j] == "D":
                    storeMapList[i+1][j] = "O" # when the player is "on top" of the slot where we put the block (B)
                    storeMapList[i][j] = "-"
                    return storeMapList
                
                if storeMapList[i+1][j] == "X": 
                    if storeMapList[i+2][j] != "#":
                        storeMapList[i][j] = "-"
                        storeMapList[i+2][j] = "X"
                        storeMapList[i+1][j] = "O"
                        return storeMapList
            
            
            elif storeMapList[i][j] == "O":
                if storeMapList[i+2][j] != "#":
                    if storeMapList[i+1][j] == "B":
                        if storeMapList[i+2][j] != "D":
                            storeMapList[i+2][j] = "B"
                            storeMapList[i][j] = "D"
                            storeMapList[i+1][j] = "P"
                            return storeMapList 
                    if storeMapList[i+1][j] == "B":
                        if storeMapList[i+2][j] == "D":
                            storeMapList[i+2][j] = "X"
                            storeMapList[i][j] = "D"
                            storeMapList[i+1][j] = "P"
                            return storeMapList 
                    elif storeMapList[i+1][j] == "X": #is changed here
                        storeMapList[i][j] = "D"
                        storeMapList[i+1][j] = "O"
                        storeMapList[i+2][j] = "B"
                        return storeMapList
                    else:
                        storeMapList[i][j] = "D"
                        storeMapList[i+1][j] = "P" 
                        return storeMapList
                  
def moveRIGHT(storeMapList):
    for i in range(len(storeMapList)):
        for j in range(len(storeMapList[i])):
            if storeMapList[i][j] == "P":
                if storeMapList[i][j+1] != "#":
                    if storeMapList[i][j+1] == "B":
                        if storeMapList[i][j+2] == "-":
                            storeMapList[i][j+1], storeMapList[i][j+2] = storeMapList[i][j+2], storeMapList[i][j+1] #switches the block (B) in the list with the space(-)
                            storeMapList[i][j], storeMapList[i][j+1] = storeMapList[i][j+1], storeMapList[i][j] #switches the player (P) with the space (-)
                            return storeMapList
                        if storeMapList[i][j+2] == "B": # Player moves a block through another block (the player is not allowed to move the block)
                            return None
                        if storeMapList[i][j+2] == "#": # Player collides with a wall (the player is not allowed to go through a wall)
                            return None
                        if storeMapList[i][j+2] == "D":
                            storeMapList[i][j+2] = "X" #block is placed in the correct slot
                            storeMapList[i][j+1] = "-"
                            storeMapList[i][j], storeMapList[i][j+1] = storeMapList[i][j+1], storeMapList[i][j]
                            return storeMapList
                    elif storeMapList[i][j+1] == "-":
                        storeMapList[i][j], storeMapList[i][j+1] = storeMapList[i][j+1], storeMapList[i][j]
                        return storeMapList 
                    
                if storeMapList[i][j+1] == "D":
                    storeMapList[i][j+1] = "O" # when the player is "on top" of the slot where we put the block (B)
                    storeMapList[i][j] = "-"
                    return storeMapList
                
                if storeMapList[i][j+1] == "X":
                    if storeMapList[i][j+2] != "#":
                        storeMapList[i][j] = "-"
                        storeMapList[i][j+2] = "B"
                        storeMapList[i][j+1] = "O"
                        return storeMapList
            
            
            elif storeMapList[i][j] == "O":
                if storeMapList[i][j+2] != "#":
                    if storeMapList[i][j+1] == "B":
                        storeMapList[i][j+2] = "B"
                        storeMapList[i][j] = "D"
                        storeMapList[i][j+1] = "P"
                        return storeMapList  
                    else:
                        storeMapList[i][j] = "D"
                        storeMapList[i][j+1] = "P"
                        return storeMapList 
                    
def moveLEFT(storeMapList):
    for i in range(len(storeMapList)):
        for j in range(len(storeMapList[i])):
            if storeMapList[i][j] == "P":
                if storeMapList[i][j-1] != "#":
                    if storeMapList[i][j-1] == "B":
                        if storeMapList[i][j-2] == "-":
                            storeMapList[i][j-1], storeMapList[i][j-2] = storeMapList[i][j-2], storeMapList[i][j-1] #switches the block (B) in the list with the space(-)
                            storeMapList[i][j], storeMapList[i][j-1] = storeMapList[i][j-1], storeMapList[i][j] #switches the player (P) with the space (-)
                            return storeMapList
                        if storeMapList[i][j-2] == "B":
                            return None
                        if storeMapList[i][j-2] == "#":
                            return None
                        if storeMapList[i][j-2] == "D":
                            storeMapList[i][j-2] = "X" #block is placed in the correct slot
                            storeMapList[i][j-1] = "-"
                            storeMapList[i][j], storeMapList[i][j-1] = storeMapList[i][j-1], storeMapList[i][j]
                            return storeMapList
                    elif storeMapList[i][j-1] == "-":
                        storeMapList[i][j], storeMapList[i][j-1] = storeMapList[i][j-1], storeMapList[i][j]
                        return storeMapList 
                    
                if storeMapList[i][j-1] == "D":
                    storeMapList[i][j-1] = "O" # when the player is "on top" of the slot where we put the block (B)
                    storeMapList[i][j] = "-"
                    return storeMapList
                
                if storeMapList[i][j-1] == "X":
                    if storeMapList[i][j-2] != "#":
                        storeMapList[i][j] = "-"
                        storeMapList[i][j-2] = "B"
                        storeMapList[i][j-1] = "O"
                        return storeMapList
            
            
            elif storeMapList[i][j] == "O":
                if storeMapList[i][j-2] != "#":
                    if storeMapList[i][j-1] == "B":
                        storeMapList[i][j-2] = "B"
                        storeMapList[i][j] = "D"
                        storeMapList[i][j-1] = "P"
                        return storeMapList  
                    else:
                        storeMapList[i][j] = "D"
                        storeMapList[i][j-1] = "P" 

#WASD for the movement in the Game when a key/letter is inputted by the player        
def movementKey(keyHandler, storeMapList): 
    if keyHandler.lower() == "w":
        moveUP(storeMapList)

    elif keyHandler.lower() == "s":
        moveDOWN(storeMapList)
        
    elif keyHandler.lower() == "d":
        moveRIGHT(storeMapList)
    
    elif keyHandler.lower() == "a":
        moveLEFT(storeMapList)
         
#SAVING FUNCTION   
def save(storeMapList, uniqueID):
    fileHandler = open("saved.txt", "w")
    fileHandler.write(uniqueID + "\n")
    for mapList in storeMapList:
        for value in mapList:
            fileHandler.write(value)
        fileHandler.write("\n")
    fileHandler.close()    
    print("Progress saved succesfully!")
    print("="*150)
    continueOptionChoice1()

#next save iteration
def save2(storeMapList):
    fileHandler = open("saved.txt", "w")
    for mapList in storeMapList:
        for value in mapList:
            fileHandler.write(value)
        fileHandler.write("\n")
    fileHandler.close() 
    print("Progress saved succesfully!")
    print("="*150)
    continueOptionChoice2()

#function that asks for the player input, then decides what to do after input
def continueOptionChoice1():
    print("OPTION-[0]: QUIT AND GO TO MAIN MENU")
    print("OPTION-[1]: QUIT SOKOBAN GAME")
    continueOption = int(input("PLEASE SELECT AN OPTION: "))
    if continueOption == 0:
        gameMMenu(storeMapList) #goes to main menu 
    elif continueOption == 1:
        exit() #quits the game
    else:
        print("Input a valid option") #if invalid asks for the user input again
        continueOptionChoice1()

def continueOptionChoice2():
    print("OPTION-[0]: QUIT AND GO TO MAIN MENU")
    print("OPTION-[1]: QUIT SOKOBAN GAME")
    continueOption = int(input("PLEASE SELECT AN OPTION: "))
    if continueOption == 0:
        gameMMenu(storeMapList)
    elif continueOption == 1:
        exit()
    else:
        print("Input a valid option")
        continueOptionChoice2()

#victory screen for 10x10 grid
def victory10(timeStart, timeEnd, saveTimeArray1):
    print()
    congrats()
    progress = int(timeEnd - timeStart)
    saveTimeArray1.append(progress)
    saveTime10(saveTimeArray1)
    print("You spent:", progress, "seconds in solving")
    print()
    viewHighScore = input("Press [1] to see the TOP SCORER | PRESS ANY BUTTON TO QUIT: ")
    if viewHighScore == "1":
        saveTimeArray1 = readTime10()
        saveTimeArray1.sort()
        print("=" * 150)
        print("Top Score(in seconds)-10x10:", saveTimeArray1[0])
        for i in range(len(saveTimeArray1)):
            if saveTimeArray1[i] == str(progress):
                print("Your place is: ", end=" ")
                print(i+1)
                print("=" * 150)
                break
    else:
        exit()
    exit()

#victory screen for 15x15
def victory15(timeStart, timeEnd, saveTimeArray2):
    print()
    congrats()
    progress = int(timeEnd - timeStart)
    saveTimeArray2.append(progress)
    saveTime15(saveTimeArray2)
    print("You spent:", progress, "seconds in solving")
    print()
    viewHighScore = input("Press [1] to see the TOP SCORER | PRESS ANY BUTTON TO QUIT: ")
    if viewHighScore == "1":
        saveTimeArray2 = readTime15()
        saveTimeArray2.sort()
        print("=" * 150)
        print("Top Score(in seconds)-15x15:", saveTimeArray2[0])
        for i in range(len(saveTimeArray2)):
            if saveTimeArray2[i] == str(progress):
                print("Your place is: ", end=" ")
                print(i+1)
                print("=" * 150)
                break
    else:
        exit()
    exit()

def loadVictory10(): #FOR RESUME 10X10 MODE
    print()
    congrats()
    saveProgressArray = loadProgress()             #load the array from text file
    totalTime = 0
    for sumAllTime in saveProgressArray:                   #summing all times
        totalTime = totalTime + int(sumAllTime)
    print("You spent:", totalTime, "seconds in  solving")
    sumArray = []
    sumArray.append(totalTime)
    saveTime10(sumArray)
    print()
    viewHighScore = input("Press [1] to see the TOP SCORER | PRESS ANY BUTTON TO QUIT: ")
    if viewHighScore == "1":
        saveTimeArray1 = readTime10()
        saveTimeArray1.sort()
        print("=" * 150)
        print("Top Score(in seconds)-10x10:", saveTimeArray1[0])
        for i in range(len(saveTimeArray1)):
            if saveTimeArray1[i] == str(totalTime):
                print("Your place is: ", end=" ")
                print(i+1)
                print("=" * 150)
                break
    else:
        exit()
    exit()

def loadVictory15(): #FOR RESUME 15X15 MODE
    print()
    congrats()
    saveProgressArray = loadProgress()             #load the array from text file
    totalTime = 0
    for sumAllTime in saveProgressArray:                   #summing all times
        totalTime = totalTime + int(sumAllTime)
    print("You spent:", totalTime, "seconds in solving")
    sumArray = []
    sumArray.append(totalTime)
    saveTime15(sumArray)
    print()
    viewHighScore = input("Press [1] to see the TOP SCORER | PRESS ANY BUTTON TO QUIT: ")
    if viewHighScore == "1":
        saveTimeArray2 = readTime15()
        saveTimeArray2.sort()
        print("=" * 150)
        print("Top Score(in seconds)-15x15:", saveTimeArray2[0], "seconds")
        for i in range(len(saveTimeArray2)):
            if saveTimeArray2[i] == str(totalTime):
                print("Your place is: ", end=" ")
                print(i+1)
                print("=" * 150)
                break
    else:
        exit()
    exit()

#Sokoban Directions
def directions():
    print("SEE THE DIRECTIONS PROVIDED BELOW:")
    print("Game Elements: (B - Box to be pushed) - (# - Wall that the Player or P can't go through) - ('-' - The spaces where the player can move) - (P - The player you can control)")
    print("*KEEP IN MIND ('B' will turn to 'X' when it's in the proper slot/destination (D))")
    print("Movement Keys: (w Key - UP) (a Key - Left) (s Key - Down) (d Key - Right)")
       
#checks the player's movement for a 10x10 grid -> once all the blocks are in the place execute for victory
def sokobanControl10(timeStart): 
    
    storeMapList = loadMap10(indexFile)
    level = True
    while level:
        sys_clr()
        directions()
        print("10x10: Level-1")
        printSoko(storeMapList)
        blockCounter = 0
        for i in storeMapList:
            for j in i:
                if j == "B":
                    blockCounter += 1
        if blockCounter > 0: #main controls during the game
            print("OPTION-[1] SAVE THE GAME AND EXIT") 
            print("OPTION-[0] QUIT WITHOUT SAVING")
            print("=" * 150)       
            keyHandler = input("Enter an option: ")
            if keyHandler == "1": #saving process
                uniqueID = "10x10Level1"  #uniqueID for the saved file in the first level (10x10)
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter) #saves the current time after saving in a list
                saveProgress(saveProgressArray)
                save(storeMapList, uniqueID)
                return None
            elif keyHandler == "0": #exits if the input is zero
                goodbyeUser()
                exit()
            movementKey(keyHandler, storeMapList)
        elif blockCounter == 0: #if all blocks are placed in the destination of the level

            level = False

    storeMapList = loadMap10(indexFile+1) #iterate to this level after finishing the first one
    level = True
    while level:
        sys_clr()
        directions()
        print("10x10: Level-2")
        printSoko(storeMapList)
        blockCounter = 0
        for i in storeMapList:
            for j in i:
                if j == "B":
                    blockCounter += 1
        if blockCounter > 0:  
            print()
            print("OPTION-[1] SAVE THE GAME AND EXIT") 
            print("OPTION-[0] QUIT WITHOUT SAVING")
            print("=" * 150)         
            keyHandler = input("Enter an option: ")
            if keyHandler == "1":
                uniqueID = "10x10Level2" #uniqueID for the saved file in the second level (10x10) -> accessed once the first level is finished
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter)
                saveProgress(saveProgressArray)
                save(storeMapList, uniqueID)
                return None
            elif keyHandler == "0":
                goodbyeUser()
                exit()
            movementKey(keyHandler, storeMapList)
        elif blockCounter == 0:
            timeEnd = time.time()
            victory10(timeStart, timeEnd, saveTimeArray1)
            level = False
        
        
    victory10()


#checks the player's movement for a 15x15 grid -> once all the blocks are in the place execute for victory
def sokobanControl15(timeStart):
    storeMapList = loadMap15(indexFile)
    level = True
    while level:
        sys_clr()
        directions()
        print()
        #timeStart = time.time()
        print("15x15: Level-1")
        print()
        printSoko(storeMapList)
        blockCounter = 0
        for i in storeMapList:
            for j in i:
                if j == "B":
                    blockCounter += 1
        if blockCounter > 0: 
            print()
            print("OPTION-[1] SAVE THE GAME AND EXIT") 
            print("OPTION-[0] QUIT WITHOUT SAVING")
            print("=" * 150)          
            keyHandler = input("Enter an option: ")
            if keyHandler == "1":
                uniqueID = "15x15Level1" #uniqueID for the saved file in the first level (15x15)
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter)
                saveProgress(saveProgressArray)
                save(storeMapList, uniqueID)
                return None
            elif keyHandler == "0":
                goodbyeUser()
                exit()
            movementKey(keyHandler, storeMapList)
        elif blockCounter == 0:
            level = False

    #second level 15x15
    storeMapList = loadMap15(indexFile+1)
    level = True
    while level:
        sys_clr()
        directions()
        print("15x15: Level-2")
        printSoko(storeMapList)
        blockCounter = 0
        for i in storeMapList:
            for j in i:
                if j == "B":
                    blockCounter += 1
        if blockCounter > 0: 
            print()
            print("OPTION-[1] SAVE THE GAME AND EXIT") 
            print("OPTION-[0] QUIT WITHOUT SAVING")
            print("=" * 150)          
            keyHandler = input("Enter an option: ")
            if keyHandler == "1":
                uniqueID = "15x15Level2" #uniqueID for the saved file in the second level (15x15) -> accessed once the first level is finished
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter)
                saveProgress(saveProgressArray)
                save(storeMapList, uniqueID)
                return None
            elif keyHandler == "0":
                goodbyeUser()
                exit()
            movementKey(keyHandler, storeMapList)
        elif blockCounter == 0:
            timeEnd = time.time()
            victory15(timeStart, timeEnd, saveTimeArray2)
            level = False
    victory15()        
   
#Creating a New Game of 10x10 or 15x15      
def gameMode(option):
    print()
    if option == 1:
        #overwrites previous saved; deletes previously saved file (if existing)
        overwriteProgress() 
        timeStart = time.time() #starts timer
        #Open 10x10 Grid Level -> Displays 1st level then proceeds with the 2nd after finishing
        sokobanControl10(timeStart) 
    elif option == 2:
        #overwrites previous saved; deletes previously saved file (if existing)
        overwriteProgress()
        timeStart = time.time()#starts timer
        #Open 10x10 Grid Level -> Displays 1st level then proceeds with the 2nd after finishing
        sokobanControl15(timeStart)
    else:
        invalidOption() #option is invalid proceed to ask for user input again
        print("=" * 150)
        gameMenu()
        
#Function for asking input on user whether what mode they want to play
def gameMenu():
    designedGameMode()
    tenbyten()
    fifteenbyfifteen()
    print("=" * 150)
    option = int(input("Enter a game mode from above (Type 1 for 10x10|Type 2 for 15x15): "))
    gameMode(option) 

#Access Last Saved Game
def recentGame(storeMapList, timeStart):
    sys_clr()
    unique_codeLVL = ""
    #try-catch
    try: #checks if the game has an existing saved file, if there is none it passes to the catch to get the exception and error set
        gotData = storeMapList[0]
        for characters in gotData:
            unique_codeLVL = unique_codeLVL + characters
    except (IndexError, ValueError):
        gotData = "No Saved File, Play a New Game First"
        print(gotData)
        gameMMenu(storeMapList)

    
    if unique_codeLVL == "10x10Level1": #uniqueID for the saved file in the first level (10x10)
        level = True
        while level:
            sys_clr()
            directions()
            print("10x10: Level-1")
            printSoko2(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0:
                print()
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)       
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save2(storeMapList)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                level = False
        
        #iterate proceeds to the second level of 10x10 Grid        
        storeMapList = loadMap10(indexFile+1)
        level = True
        while level:
            sys_clr()
            directions()
            print("10x10: Level-2")
            printSoko(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0:  
                print()
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)         
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    uniqueID = "10x10Level2" #uniqueID for the saved file in the second level (10x10) -> accessed once the first level is finished
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save(storeMapList, uniqueID)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                loadVictory10()
                level = False

    elif unique_codeLVL == "10x10Level2": #uniqueID for the saved file in the second level (10x10)
        level = True
        while level:
            sys_clr()
            directions()
            print("10x10: Level-2")
            printSoko2(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0:
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)         
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save2(storeMapList)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter)
                saveProgress(saveProgressArray)
                loadVictory10()
                level = False
  
    elif unique_codeLVL == "15x15Level1": #uniqueID for the saved file in the first level (15x15)
        level = True
        while level:
            sys_clr()
            directions()
            print("15x15: Level-1")
            printSoko2(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0:
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)          
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save2(storeMapList)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                level = False

        #iterate proceeds to the second level of 15x15 Grid 
        storeMapList = loadMap15(indexFile+1)
        level = True
        while level:
            sys_clr()
            directions()
            print("15x15:Level-2")
            printSoko(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0: 
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)          
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    uniqueID = "15x15Level2" #uniqueID for the saved file in the second level (15x15) -> accessed once the first level is finished
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save(storeMapList, uniqueID)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                loadVictory15()
                level = False   
                
    elif unique_codeLVL == "15x15Level2": #uniqueID for the saved file in the second level (15x15)
        level = True
        while level:
            sys_clr()
            directions()
            print("15x15:Level-2")
            printSoko2(storeMapList)
            blockCounter = 0
            for i in storeMapList:
                for j in i:
                    if j == "B":
                        blockCounter += 1
            if blockCounter > 0: 
                print()
                print("OPTION-[1] SAVE THE GAME AND EXIT") 
                print("OPTION-[0] QUIT WITHOUT SAVING")
                print("=" * 150)          
                keyHandler = input("Enter an option: ")
                if keyHandler == "1":
                    timeEnd = time.time()
                    progress_counter = int(timeEnd - timeStart)
                    saveProgressArray.append(progress_counter)
                    saveProgress(saveProgressArray)
                    save2(storeMapList)
                    return None
                elif keyHandler == "0":
                    goodbyeUser()
                    exit()
                movementKey(keyHandler, storeMapList)
            elif blockCounter == 0:
                timeEnd = time.time()
                progress_counter = int(timeEnd - timeStart)
                saveProgressArray.append(progress_counter)
                saveProgress(saveProgressArray)
                loadVictory15()
                level = False 
    
#DISPLAY HIGHSCORES IN MENU
def gameHigh():
    sys_clr()
    print("=" * 150)
    designedHighscore()
    #try catch if there is no saved level in the 10x10
    try:
        saveTimeArray1 = readTime10()
        saveTimeArray1.sort()
        print("10x10 GRID HIGHSCORE:", saveTimeArray1[0], "seconds")
    except(IndexError, ValueError):
        saveTimeArray1 = "10x10 Grid: No Scores Yet"
        print(saveTimeArray1)

    #try catch if there is no saved level in the 15x15
    try:
        saveTimeArray2 = readTime15()
        saveTimeArray2.sort()
        print("15X15 GRID HIGHSCORE:", saveTimeArray2[0], "seconds")
        print("=" * 150)
        
    except (IndexError, ValueError):
        saveTimeArray2 = "15x15 Grid: No Scores Yet"
        print(saveTimeArray2)
    gameMMenu(storeMapList)
 
#Main Menu for user navigation   
def gameMMenu(storeMapList):
    titleforMainMenu()
    print("OPTION [0] - SHOW SOKOBAN HIGHSCORE ")
    print("OPTION [1] - START A NEW GAME")
    print("OPTION [2] - LOAD LAST GAME SAVED")
    print("OPTION [3] - EXIT GAME")
    print()
    #MAIN MENU OPTION
    option1 = int(input("ENTER OPTION: ")) 
    
    #AFTER CHOOSING AN OPTION, HERE ARE THE CONDITIONS FOR EACH OPTION
    if option1 == 0:
        #OPENS FUNCTION THAT SHOWS THE HIGHSCORE
        gameHigh()
    elif option1 == 1:
        #OPENS MENU FOR SELECTING A GAME LEVEL
        gameMenu()
    elif option1 == 2:
        #ACCESSES LAST SAVED MAP THEN CONTINUES THE TIME
        storeMapList = loadMapSaved()
        timeStart = time.time()
        recentGame(storeMapList, timeStart)
    elif option1 == 3:
        #USER EXITS PRINTS 
        goodbyeUser()
        exit()
    else: 
        #INVALID OPTION IS SELECTED PRINTS THEN RETURNS TO THE MENU
        invalidOption()
        print("="*150)
        gameMMenu(storeMapList)
        
#Sokoban Entry Screen
def welcomePlayer(storeMapList):
    sys_clr()
    title()
    print("Please Select An Option")
    print("="*150)
    gameMMenu(storeMapList)

def title():
    print("""  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |  
| ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |  
| |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |  
| |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |  
| |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |  
| |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
                                                       .----------------.  .----------------.                                                 
                                                      | .--------------. || .--------------. |                                                
                                                      | |  _________   | || |     ____     | |                                                
                                                      | | |  _   _  |  | || |   .'    `.   | |                                                
                                                      | | |_/ | | \_|  | || |  /  .--.  \  | |                                                
                                                      | |     | |      | || |  | |    | |  | |                                                
                                                      | |    _| |_     | || |  \  `--'  /  | |                                                
                                                      | |   |_____|    | || |   `.____.'   | |                                                
                                                      | |              | || |              | |                                                
                                                      | '--------------' || '--------------' |                                                
                                                       '----------------'  '----------------'                                                 
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.  
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |    _______   | || |     ____     | || |  ___  ____   | || |     ____     | || |   ______     | || |      __      | || | ____  _____  | |  
| |   /  ___  |  | || |   .'    `.   | || | |_  ||_  _|  | || |   .'    `.   | || |  |_   _ \    | || |     /  \     | || ||_   \|_   _| | |  
| |  |  (__ \_|  | || |  /  .--.  \  | || |   | |_/ /    | || |  /  .--.  \  | || |    | |_) |   | || |    / /\ \    | || |  |   \ | |   | |  
| |   '.___`-.   | || |  | |    | |  | || |   |  __'.    | || |  | |    | |  | || |    |  __'.   | || |   / ____ \   | || |  | |\ \| |   | |  
| |  |`\____) |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__) |  | || | _/ /    \ \_ | || | _| |_\   |_  | |  
| |  |_______.'  | || |   `.____.'   | || | |____||____| | || |   `.____.'   | || |  |_______/   | || ||____|  |____|| || ||_____|\____| | |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  """)

def titleforMainMenu():
    print(""" .----------------.  .----------------.  .----------------.  .-----------------.   .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || |     _____    | || | ____  _____  | |  | | ____    ____ | || |  _________   | || | ____  _____  | || | _____  _____ | |
| ||_   \  /   _|| || |     /  \     | || |    |_   _|   | || ||_   \|_   _| | |  | ||_   \  /   _|| || | |_   ___  |  | || ||_   \|_   _| | || ||_   _||_   _|| |
| |  |   \/   |  | || |    / /\ \    | || |      | |     | || |  |   \ | |   | |  | |  |   \/   |  | || |   | |_  \_|  | || |  |   \ | |   | || |  | |    | |  | |
| |  | |\  /| |  | || |   / ____ \   | || |      | |     | || |  | |\ \| |   | |  | |  | |\  /| |  | || |   |  _|  _   | || |  | |\ \| |   | || |  | '    ' |  | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |     _| |_    | || | _| |_\   |_  | |  | | _| |_\/_| |_ | || |  _| |___/ |  | || | _| |_\   |_  | || |   \ `--' /   | |
| ||_____||_____|| || ||____|  |____|| || |    |_____|   | || ||_____|\____| | |  | ||_____||_____|| || | |_________|  | || ||_____|\____| | || |    `.__.'    | |
| |              | || |              | || |              | || |              | |  | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'    '----------------'  '----------------'  '----------------'  '----------------' """)


def goodbyeUser():
    print(""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |     ____     | || |     ____     | || |  ________    | || |   ______     | || |  ____  ____  | || |  _________   | |
| |  .' ___  |   | || |   .'    `.   | || |   .'    `.   | || | |_   ___ `.  | || |  |_   _ \    | || | |_  _||_  _| | || | |_   ___  |  | |
| | / .'   \_|   | || |  /  .--.  \  | || |  /  .--.  \  | || |   | |   `. \ | || |    | |_) |   | || |   \ \  / /   | || |   | |_  \_|  | |
| | | |    ____  | || |  | |    | |  | || |  | |    | |  | || |   | |    | | | || |    |  __'.   | || |    \ \/ /    | || |   |  _|  _   | |
| | \ `.___]  _| | || |  \  `--'  /  | || |  \  `--'  /  | || |  _| |___.' / | || |   _| |__) |  | || |    _|  |_    | || |  _| |___/ |  | |
| |  `._____.'   | || |   `.____.'   | || |   `.____.'   | || | |________.'  | || |  |_______/   | || |   |______|   | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

def invalidOption():
    print(""" .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || | ____  _____  | || | ____   ____  | || |      __      | || |   _____      | || |     _____    | || |  ________    | |
| |    |_   _|   | || ||_   \|_   _| | || ||_  _| |_  _| | || |     /  \     | || |  |_   _|     | || |    |_   _|   | || | |_   ___ `.  | |
| |      | |     | || |  |   \ | |   | || |  \ \   / /   | || |    / /\ \    | || |    | |       | || |      | |     | || |   | |   `. \ | |
| |      | |     | || |  | |\ \| |   | || |   \ \ / /    | || |   / ____ \   | || |    | |   _   | || |      | |     | || |   | |    | | | |
| |     _| |_    | || | _| |_\   |_  | || |    \ ' /     | || | _/ /    \ \_ | || |   _| |__/ |  | || |     _| |_    | || |  _| |___.' / | |
| |    |_____|   | || ||_____|\____| | || |     \_/      | || ||____|  |____|| || |  |________|  | || |    |_____|   | || | |________.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

def designedHighscore():
    print(""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     _____    | || |    ______    | || |  ____  ____  | || |    _______   | || |     ______   | || |     ____     | || |  _______     | || |  _________   | || |    _______   | |
| | |_   ||   _| | || |    |_   _|   | || |  .' ___  |   | || | |_   ||   _| | || |   /  ___  |  | || |   .' ___  |  | || |   .'    `.   | || | |_   __ \    | || | |_   ___  |  | || |   /  ___  |  | |
| |   | |__| |   | || |      | |     | || | / .'   \_|   | || |   | |__| |   | || |  |  (__ \_|  | || |  / .'   \_|  | || |  /  .--.  \  | || |   | |__) |   | || |   | |_  \_|  | || |  |  (__ \_|  | |
| |   |  __  |   | || |      | |     | || | | |    ____  | || |   |  __  |   | || |   '.___`-.   | || |  | |         | || |  | |    | |  | || |   |  __ /    | || |   |  _|  _   | || |   '.___`-.   | |
| |  _| |  | |_  | || |     _| |_    | || | \ `.___]  _| | || |  _| |  | |_  | || |  |`\____) |  | || |  \ `.___.'\  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___/ |  | || |  |`\____) |  | |
| | |____||____| | || |    |_____|   | || |  `._____.'   | || | |____||____| | || |  |_______.'  | || |   `._____.'  | || |   `.____.'   | || | |____| |___| | || | |_________|  | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

def congrats():
    print(""" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     ____     | || | ____  _____  | || |    ______    | || |  _______     | || |      __      | || |  _________   | || |    _______   | || |              | |
| |   .' ___  |  | || |   .'    `.   | || ||_   \|_   _| | || |  .' ___  |   | || | |_   __ \    | || |     /  \     | || | |  _   _  |  | || |   /  ___  |  | || |      _       | |
| |  / .'   \_|  | || |  /  .--.  \  | || |  |   \ | |   | || | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || | |_/ | | \_|  | || |  |  (__ \_|  | || |     | |      | |
| |  | |         | || |  | |    | |  | || |  | |\ \| |   | || | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |     | |      | || |   '.___`-.   | || |     | |      | |
| |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\   |_  | || | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || |    _| |_     | || |  |`\____) |  | || |     | |      | |
| |   `._____.'  | || |   `.____.'   | || ||_____|\____| | || |  `._____.'   | || | |____| |___| | || ||____|  |____|| || |   |_____|    | || |  |_______.'  | || |     |_|      | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |     (_)      | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                     .----------------.  .----------------.  .----------------.    .----------------.  .----------------.  .-----------------. .----------------.                   
                    | .--------------. || .--------------. || .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. |                  
                    | |  ____  ____  | || |     ____     | || | _____  _____ | |  | | _____  _____ | || |     _____    | || | ____  _____  | || |              | |                  
                    | | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| |  | ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || |      _       | |                  
                    | |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | |  | |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || |     | |      | |                  
                    | |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | |  | |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || |     | |      | |                  
                    | |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | |  | |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || |     | |      | |                  
                    | |   |______|   | || |   `.____.'   | || |    `.__.'    | |  | |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || |     |_|      | |                  
                    | |              | || |              | || |              | |  | |              | || |              | || |              | || |     (_)      | |                  
                    | '--------------' || '--------------' || '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' |                  
                     '----------------'  '----------------'  '----------------'    '----------------'  '----------------'  '----------------'  '----------------'                   """)

def designedGameMode():
    print(""" .----------------.  .----------------.  .----------------.  .----------------.    .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | |  | | ____    ____ | || |     ____     | || |  ________    | || |  _________   | |
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |  | ||_   \  /   _|| || |   .'    `.   | || | |_   ___ `.  | || | |_   ___  |  | |
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |  | |  |   \/   |  | || |  /  .--.  \  | || |   | |   `. \ | || |   | |_  \_|  | |
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |  | |  | |\  /| |  | || |  | |    | |  | || |   | |    | | | || |   |  _|  _   | |
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |  | | _| |_\/_| |_ | || |  \  `--'  /  | || |  _| |___.' / | || |  _| |___/ |  | |
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |  | ||_____||_____|| || |   `.____.'   | || | |________.'  | || | |_________|  | |
| |              | || |              | || |              | || |              | |  | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'    '----------------'  '----------------'  '----------------'  '----------------' """)

def tenbyten():
    print(""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     __       | || |     ____     | || |  ____  ____  | || |     __       | || |     ____     | |
| |    /  |      | || |   .'    '.   | || | |_  _||_  _| | || |    /  |      | || |   .'    '.   | |
| |    `| |      | || |  |  .--.  |  | || |   \ \  / /   | || |    `| |      | || |  |  .--.  |  | |
| |     | |      | || |  | |    | |  | || |    > `' <    | || |     | |      | || |  | |    | |  | |
| |    _| |_     | || |  |  `--'  |  | || |  _/ /'`\ \_  | || |    _| |_     | || |  |  `--'  |  | |
| |   |_____|    | || |   '.____.'   | || | |____||____| | || |   |_____|    | || |   '.____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

def fifteenbyfifteen():
    print(""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     __       | || |   _______    | || |  ____  ____  | || |     __       | || |   _______    | |
| |    /  |      | || |  |  _____|   | || | |_  _||_  _| | || |    /  |      | || |  |  _____|   | |
| |    `| |      | || |  | |____     | || |   \ \  / /   | || |    `| |      | || |  | |____     | |
| |     | |      | || |  '_.____''.  | || |    > `' <    | || |     | |      | || |  '_.____''.  | |
| |    _| |_     | || |  | \____) |  | || |  _/ /'`\ \_  | || |    _| |_     | || |  | \____) |  | |
| |   |_____|    | || |   \______.'  | || | |____||____| | || |   |_____|    | || |   \______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

#Main Code
storeMapList = loadMap10(indexFile)
welcomePlayer(storeMapList)




        
        