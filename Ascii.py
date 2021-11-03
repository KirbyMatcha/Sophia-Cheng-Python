y = input("What is your string? ")
a = [ord(character) for character in y]
for x in y:
    answer = x + " = {}"
    print(answer.format(a))



y = input("What is your string? ")

a = [ord(character) for character in y]
for x in y:
    print(x)




