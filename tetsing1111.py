def main_menu():
    import os
    clearConsole = lambda:os.system('cls')
    clearConsole()
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
    b = "7", "8", "9"
    while y != "x":
        if y == "1":
            HelloWorld()
            clearConsole()
            main_menu()
        elif y == "2":
            GoodbyeWorld()
            clearConsole()
            main_menu()            
        elif y == "3":
            GoodbyePerson()
            clearConsole()
            main_menu()
        elif y == "4":
            GoodTeacher()
            clearConsole()
            main_menu()
        elif y == "5":
            forLoop()
            clearConsole()
            main_menu()
        elif y == "6":
            whileLoop()
            clearConsole()
            main_menu()
        elif y == b:
            invalid()
            clearConsole()
            main_menu()
        else:
            exit()
        

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