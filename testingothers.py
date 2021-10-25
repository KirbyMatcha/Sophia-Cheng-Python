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