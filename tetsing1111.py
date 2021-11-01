

b = "7", "8", "9"
a = "1", "2", "3", "4", "5", "6"
c = a, b

def main_menu():
    import os

    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

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
    while y != "x":
        if y == "1":
            HelloWorld()
            main_menu()
        elif y == "2":
            GoodbyeWorld()
            main_menu()          
        elif y == "3":
            GoodbyePerson()
            main_menu()
        elif y == "4":
            GoodTeacher()
            main_menu()
        elif y == "5":
            forLoop()
            main_menu()
        elif y == "6":
            whileLoop()
            main_menu()
        else:
            invalid()
            main_menu()
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")
    input("Press Enter to continue ")
    quit()

    
        

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
        print("")
        print("----End of Output -----------------------------")
        print("")
        print("")
        print("")
        input("Press Enter to continue")

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