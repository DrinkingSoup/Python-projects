#author: Adam Uremek

#Variables
Active = True

#Inital inputs (assumed to not need error checking)
stringOne = input("Please Enter A String: ")
stringTwo = input("Please Enter A Second String: ")



#Loop Start
while Active:
    userCommand = input("What would you like to do?\na (add indel)\nd (delete indel)\ns (score)\nq (quit)\n")

#Controls addition of indel (a)
    if userCommand.casefold() == "a":
        stringInput = input("which string would you like to add to?\n1 (string 1)\n2 (string 2)\n")
    #String 1 condition
        if stringInput == "1":
            stringIndex = input("Enter the index number you would like changed (starting at 0)\n")
            if int(stringIndex) >=0 and int(stringIndex) <= len(stringOne) - 1:
                stringOne = stringOne[0:int(stringIndex)] + "-" + stringOne[int(stringIndex):len(stringOne)]
                stringTwo = stringTwo + "-"
            else:
                print("Error: Invalid Index")
                Active = False
    #String 2 Condition
        elif stringInput == "2":
            stringIndex = input("Enter the index number you would like changed (starting at 0)\n")
            if int(stringIndex) >=0 and int(stringIndex) <= len(stringOne) - 1:
                stringTwo = stringTwo[0:int(stringIndex)] + "-" + stringTwo[int(stringIndex):len(stringTwo)]
                stringOne = stringOne + "-"
            else:
                print("Error: Invalid Index")
                Active = False
    #Error Check
        else:
            print("Error: Invalid String Input")
            Active = False

#Controls deletion of indel (d)
    elif userCommand.casefold() == "d":
        stringInput = input("Which string would you like to delete from?\n1 (string 1)\n2 (string 2)\n")
    #String 1 condition
        if stringInput == "1":
            stringIndex = input("Enter the index number you would like changed (starting at 0)\n")
            if int(stringIndex) >=0 and int(stringIndex) <= (len(stringOne) - 1) and stringOne[int(stringIndex)] == "-" and int(stringIndex) !=(len(stringOne) - 1):
                stringOne = stringOne[:int(stringIndex)] + stringOne[int(stringIndex) + 1:]
                stringTwo = stringTwo[:-1]
            else:
                print("Error: Invalid Index")
                Active = False
    #String 2 Condition
        elif stringInput == "2":
            stringIndex = input("Enter the index of the character you would like to add an indel (starting at 0)\n")
            if int(stringIndex) >=0 and int(stringIndex) <= (len(stringOne) - 1) and stringTwo[int(stringIndex)] == "-" and int(stringIndex) !=(len(stringTwo) - 1):
                stringTwo = stringTwo[:int(stringIndex)] + stringtwo[int(stringIndex) + 1:]
                stringOne = stringOne[:-1]
            else:
                print("Error: Invalid Index")
                Active = False
    #Error Check
        else:
            print("Error: Invalid String Input")
            Active = False

#Calculates and displays the matches and mismatches (s)
    elif userCommand.casefold() == "s":
    #Temporary variables used to calculate matches and mismatches
        tempStringOne = stringOne
        tempStringTwo = stringTwo
        matchNum = 0
        mismatchNum = 0
        maxLength = 0
    #Calculation and printing of matches and mismatches
        if len(stringOne) > len(stringTwo):
            maxLength = len(stringOne)
            tempStringTwo = stringTwo + ("-" * (maxLength - len(stringTwo)))
        else:
            maxLength = len(stringTwo)
            tempStringOne = stringOne + ("-" * (maxLength - len(stringOne)))

        for char in range(maxLength):
            if tempStringOne[char].casefold() == tempStringTwo[char].casefold():
                matchNum += 1
            else:
                mismatchNum += 1
        print("Matches: " + str(matchNum))
        print("Mismatches: " + str(mismatchNum))


#Exits the running program
    elif userCommand.casefold() == "q":
        Active = False

#Shuts down program when no initial value is vlaid
    else:
        print("Error: Invalid Input")
        Active = False
#Lists the current DNA strings
    if Active:
        print(stringOne)
        print(stringTwo)

#  :D