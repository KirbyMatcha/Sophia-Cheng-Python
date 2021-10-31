def main_menu():
    import os
    os.system('cls')
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
    print("")
    print("----Start of Output ---------------------------")
    print("")
    if y == "1":
        HelloWorld()
    elif y == "2":
        GoodbyeWorld()       
    elif y == "3":
        GoodbyePerson()
    elif y == "4":
        GoodTeacher()
    elif y == "5":
        forLoop()
    elif y == "6":
        whileLoop()
    elif y == "x":
        exit()
    else:
        invalid() 
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    if y == "x":
        exit()
    else:
        input("Press Enter to continue")
        return main_menu()

def HelloWorld():
    print("Hello World")
           

def GoodbyeWorld():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def GoodbyePerson():
    print("Hello World")
    username = input("What is your name ? ")
    print("Goodbye " + username)

def GoodTeacher():
    username = input("Teacher's name (try Mr Horan) ")
    g = "Mr Horan"
    if username == g:
        print("You are lucky, he is a great teacher.")
    else:
        print(username + " is an ok teacher")

def forLoop():
    for x in range(1, 500):
        print(x)

def whileLoop():
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
        print("")

def invalid():
    print("invalid option")

def exit():
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
    input("Press Enter to continue ")
    quit()

main_menu()