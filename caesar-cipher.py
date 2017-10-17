#Uses ASCII values to encrypt your string
def ShiftLoop(Char, Shift):
    Char = int(Char)
    if Char + Shift > 126:
        return (Char + Shift - 126 + 32) #If the the sum is greater than 126, then it loops around from 32
    elif Char + Shift < 32:
        return (Char + Shift - 32 + 126) #If it is less than 32 it loops backwards from 126
    elif 32 <= Char + Shift <= 126:
        return (Char + Shift) #If it is between the range it is just returned


def ConvertToASCII(String):
    lst = []
    i = 0 #i is used for counting and lst is used to list all the characters
    for char in String:
       lst.append(str(ord(char)))
       i += 1 #Cycles throught the string converting each character to ASCII and adding it to lst
    if i == len(String):
        return lst #Once it has cycled through the entire string, it returns the list


def ReturnNewASCIIvalues(Values,FirstShift,SecondShift):
    i = 0
    lst = [] #same use as before
    for char in Values:
        while i % 2 == 0:
            lst.append(str(ShiftLoop(char, FirstShift))) #Uses the ShiftLoop function to add the ASCII values to the list after they are changed
            i += 1            
        else:
            lst.append(str(ShiftLoop(char, SecondShift)))
            i += 1 #does the same but for the odd characters
    return lst #returns all the new ASCII values as a list


def ConvertToCharacters(String):
    i = 0
    lst = [] #same use as before
    for char in String:
        lst += chr(int(char)) #add the corresponding character for each ASCII value to a list
        i += 1
    if i == len(String):
        return lst #returns all the characters


def GetShift(evenodd):
    while True:
        direction = raw_input("What direction do you want to shift towards for %s numbered characters? >>> " % evenodd )
        if direction != "-" and direction != "+":
            print "Invalid Input!"
            continue
        else:
            break
    while True:
        try:
            shift = int(raw_input("How much would you like to shift by for %s numbers (must be between 0 and 94) >>> " %evenodd )) 
            break
        except ValueError:
            print "That can not be turned into an integer try again! "
            continue
    while 0 > shift or 94 < shift:
        shift = int(raw_input("How much would you like to shift by for %s numbers (must be between 0 and 94!) >>> " %evenodd ))         
    if direction == "-":
        return (shift)*-1
    else:
        return (shift)   

def reverse(String):
    String = String[::-1]
    return String

def main():
    DecOrEnc = raw_input("Would you like to decrypt or encrypt a message? Type \"D\" for decryption and \"E\" for encryption >>> ")
    if DecOrEnc == "D" or DecOrEnc == "d":
        String = raw_input("What string would you like to decrypt? >>> ")
        theFirstShift = -1*GetShift("even")
        theSecondShift = -1*GetShift("odd")
        ASCII = ConvertToASCII(String)
        NewASCII = ReturnNewASCIIvalues(ASCII,theFirstShift,theSecondShift)
        CharBefRev = ConvertToCharacters(NewASCII)
        CharBefRev = CharBefRev[::2]
        CharAfRev = reverse(CharBefRev)
        CharAfRev = ''.join(CharAfRev)
        print ("Your decrypted string is %s, Your encrypted string is %s") % (CharAfRev, String)
    elif DecOrEnc == "E" or DecOrEnc == "e":
        String = raw_input("What string would you like to encrypt? >>> ")
        theFirstShift = GetShift("even")
        theSecondShift = GetShift("odd")
        ASCII = ConvertToASCII(String)
        NewASCII = ReturnNewASCIIvalues(ASCII,theFirstShift,theSecondShift)
        CharBefRev = ConvertToCharacters(NewASCII)
        CharBefRev = CharBefRev[::2]
        CharAfRev = reverse(CharBefRev)
        CharAfRev = ''.join(CharAfRev)
        print("Your encrypted string is %s, Your decrypted string is %s") % (String, CharAfRev)
    elif DecOrEnc != "D" or DecOrEnc == "E" or DecOrEnc == "e" or DecOrEnc == "d":
        print '\n' + "Invalid Input" + '\n'
        main()
    while True:
        Answer = raw_input("Would you like to decrypt  or encrypt another string. Answer y or n for yes or no. >>> ")
        if Answer == "y" or Answer == "Y":
            main()
        elif Answer == "n" or Answer == "N":
            print "Okay"
            break
        elif Answer != "n" or Answer != "N" or Answer != "y" or Answer != "Y":
            print "Invalid Input!"
            continue

main()
