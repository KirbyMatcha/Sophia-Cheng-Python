def main_menu():
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Sophia                               |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("")
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    y = input("Enter an option ")

    if y == "1":
        HelloWorld()
    elif y == "2":
        GoodbyeWorld()
    elif y == "3":
        GoodbyePerson()
    elif y == "4":
        GoodTeacher()
    elif y == "5":
        forLoop
    elif y == "6":
        whileLoop()
    elif y == "7":
        invalid()
    elif y == "8":
        invalid()
    elif y == "9":
        invalid()
    elif y == "x":
        print("")
        print("----Start of Output ---------------------------")
        print("")
        print("")
        print("----End of Output -----------------------------")
        print("")
        print("")
        print("")
        input("Press Enter to continue")
        exit 
    else:
        invalid()

def HelloWorld():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu()            

def GoodbyeWorld():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu()

def GoodbyePerson():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    username = input("What is your name ? ")
    print("Goodbye " + username)
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu()

def GoodTeacher():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    username = input("Teacher's name (try Mr Horan) ")
    y = "Mr Horan"
    if username == y:
        print("You are lucky, he is a great teacher.")
    else:
        print(username + " is an ok teacher")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu() 

def forLoop():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    for x in range(1, 500):
        print(x)
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu()

def whileLoop():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    y = input("What is the name of this subject ")
    i = "Not Correct - try again"
    a = "IST"
    while y != a:
        print(i)
        y = input("What is the name of this subject ")
    else:        
        print("")
        print("")
        print("Congratulations!!")
        print("")
        print("")

def invalid():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("invalid option")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    main_menu()


main_menu()