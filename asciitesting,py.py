
a = "Hello, World!"
print(len(a))

text = input("What is your string? ")
ascii_values = ['''
''']
for character in text:
    ascii_values.append(ord(character))
print(ascii_values)

text = input("What is your string? ")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
answer = "{} = {}"
for x in text:
    print(x.format(text, ascii_values)) 


text = "c"
print(ord(text))

text = input("What is your string? ")
print("The ASCII value of '" + text + "' is", ord(text)) 

y = input("What is your string? ")
ascii_values = []
for x in y:
    print(x)
    for x in y:
       ascii_values.append(ord(x))
print(ascii_values) 

text = input("What is your string? ")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
print(ascii_values)

text = input("What is your string? ")
y = ord(character) for character in text
for x in text:
    print (x + " = " + y ) 

text = input("What is your string? ")
for x in range(text):
    print(x)

text = input("What is your string? ")
for x in text:
    print(x + " = " + (ord(x)))



def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values
text = input("Enter a string: ")
print(to_ascii(text))

y = input("What is your string? ")
for x in y:
    print(x)


y = input("What is your string? ")
a = [ord(character) for character in y]
for x in y:
    answer = x + " = {}"
    print(answer.format(a))



y = input("What is your string? ")

a = [ord(character) for character in y]
for x in y:
    print(x)