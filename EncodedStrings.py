print(" ------------------------------------------------")
print("|                                                |")
print("|    09EncodeAString                             |")
print("|    Name : Sophia                               |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
y = input("What is your string? ")
b = ""
for x in y:
    a = chr(ord(x) + 1)
    print(x + "=" + a)
    b += a
    print(b)
