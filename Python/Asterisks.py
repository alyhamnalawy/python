import os
os.system("cls")
def LeftArrow():
    os.system("cls")
    print(15*"\n",end="")
    for i in range(1,6):
        print((5-i)*" ",end = "")
        print(i*"*",end = "")
        if i == 5:
            print(15*"*",end = "")
        print("")
    for i in range(1,5):
        print(i*" ",end = "")
        print((5-i)*"*",end = "")
        print("")

def RightArrow():
    os.system("cls")
    print(15*"\n",end="")
    for i in range(1,6):
        if i == 5:
            print(20*" ",end = "")
        else:
            print(35*" ",end = "")
        # Print the upper arrow
        print(i*"*",end = "")
        print((5-i)*" ",end = "")
        # Check if it's the the mid line
        if i == 5:
            print(15*"*",end = "")
        print("")
    # Print the lower arrow
    for i in range(1,5):
        print(35*" ",end = "")
        print((5-i)*"*",end = "")
        print(i*" ",end = "")
        print("")

def DownArrow():
    os.system("cls")
    # Go to origin point
    print(19*"\n",end="")
    # Print the middle line
    for i in range(1,16):
        print(20*" "+"*")
    # Print the  arrow
    for i in range(5,0,-1):
        print((20-(i-1))*" ",end="")
        print(((2*i)-1)*"*")

def UpArrow():
    os.system("cls")
    # Print the  arrow
    for i in range(1,6):
        print((20-(i-1))*" ",end="")
        print(((2*i)-1)*"*")
    # Print the middle line
    for i in range(1,16):
        print(20*" "+"*")
    



userInput = "0"
while(userInput!= "0"):
    if userInput == "1":
        LeftArrow()
    elif userInput == "2":
        RightArrow()
    elif userInput == "3":
        DownArrow()
    elif userInput == "4":
        UpArrow()




    UserInput = input()