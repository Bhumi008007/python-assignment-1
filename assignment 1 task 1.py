a = int(input("enter the first no.: "))
b = int(input("enter the second no.: "))

add = a + b
sub = a - b
multiply = a * b
if b != 0:
    division = a / b
else:
    division = "undefined"

print('result:')
print(f"add: {a}+{b}= {add}")
print(f"subtraction: {a}-{b}= {sub}")
print(f"multiply: {a}*{b}= {multiply}")
print(f"division: {a}/{b}= {division}")
