def menu():
    import os
    os.system('cls')
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Leo                                  |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print(" ")
    print("1. Hello World ")
    print("2. Goodbye World ")
    print("3. Goodbye Person ")
    print("4. Good Teacher ")
    print("5. forLoop ")
    print("6. whileLoop ")
    print("7. string Loop ")
    print("8. Convert to ascii ")
    print("9. Encode a string ")
    print("x. To Exit ")
    number = input("Enter an option ")
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    if number == "1":
        helloworld()
    elif number == "2":
        goodbyeworld()
    elif number == "3":
        goodbyeperson()
    elif number == "4":
        goodteacher()
    elif number == "5":
        forloop()
    elif number == "6":
        whileloop()
    elif number == "x":
        exit()
    else:
        print("invalid option")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
    if number == "x":
        input("Press Enter to continue ")
    else:
        input("Press Enter to continue ")
        return menu()
def helloworld():
    print("Hello World")
def goodbyeworld():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
def goodbyeperson():
    print("Hello")
    username = input("What is your name ? ")
    print("Goodbye " + username)
def goodteacher():
    x = input("Teacher's name (try Mr Horan) ")
    y = "Mr Horan"
    if x == y:
        print ("You are lucky, he is a great teacher.")
    else:
        print(x + " is an ok teacher")
def forloop():
    for x in range(1, 500):
        print(x)
def whileloop():
    i = input("What is the name of this subject ")
    while i != "IST":
        print("Not Correct - try again")
        i = input("What is the name of this subject ")
    print(" ")
    print(" ")
    print(" Congratulations!!")
    print(" ")
    print(" ")
def exit():
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
    input("Press Enter to continue ")
    quit()
menu()