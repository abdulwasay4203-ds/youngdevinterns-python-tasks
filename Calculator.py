# Simple calculator: add, subtract, multiply, divide

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation: +  -  *  / ")
op = input("Enter operation: ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b == 0:
        print("Error: division by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operation")
