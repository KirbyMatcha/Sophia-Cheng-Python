def helloworld():
    print("Hello world")

def goodbyeworld():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbyeperson():
    print("Hello")
    x=input("What is your name? ")
    print("Goodbye " + x)

def goodteacher():
    x="Mr Horan"
    y=input("Teacher's name (try Mr Horan) ")
    if y==x:
        print("You are lucky, he is a great teacher.")
    else:
        print(y + " is an ok teacher")

def forloop():
    for x in range(1,500):
        print(x)

def whileloop():
    x=input("What is the name of this subject ")
    while x!="IST":
      print("Not Correct - try again")
      x=input("What is the name of this subject ")
    else:
      print("")
      print("")
      print("Congratulations!!")
      print("")
      print("")
      print("")

def start():
    print("")
    print("----Start of Output ---------------------------")
    print("")

def end():
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to Continue ")

def x():
    print("no")


while True:
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Anna                                 |")
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
    print("8. convert to ascii")
    print("9. Encode to string")
    print("x. To Exit")
    p=input("Enter an option ")
    correct=["1","2","3","4","5","6","7","8","9","x"]
    start()
    
    if p in correct:
        if p=="x":
            print("")
            print("----End of Output -----------------------------")
            print("")
            print("")
            print("")
            input("Press Enter to Continue ")
            break

        elif p=="1":
            helloworld()
            
        elif p=="2":
            goodbyeworld()

        elif p=="3":
            goodbyeperson()

        elif p=="4":
            goodteacher()

        elif p=="5":
            forloop()

        elif p=="6":
            whileloop()

        elif p=="7":
            print("Invalid Option")

        elif p=="8":
            print("Invalid Option")

        elif p=="9":
            print("Invalid Option")
        
    else:
        print("Invalid Option")

    end()


print(" ------------------------------------------------")
print("|                                                |")
print("|    06whileLoop                                 |")
print("|    Name : Amudha Bharathi                      |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
while True:
    subject = input("What is the name of this subject ")
    if subject == "IST":
        print("")
        print("")
        print(" Congratulations!!")
        print("")
        print("")
        break
    else:
        print("Not Correct - try again")
        

a = 25
b = int(input("Type in a number"))
c = 22
if b > a:
    print("b is greater than a")
    if b > c:
        print("b is greater than c")
    else:
        print("b is less than c")
else:
    print("b is less than a")

if b == 15:
    print("Wow that's my age")

teacher = input("Teacher's name (try Mr Horan) ")
if teacher=="Mr Horan":
    print("You are lucky, he is a great teacher") 
else:
    print(teacher,"is an ok teacher")


i = 1
while i < 6:
    print(i)
    i += 1