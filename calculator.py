
# THIS WILL MANIFEST INTO A CALCULATOR!

# addition
def add(n1,n2):
    return n1 + n2

# subtraction
def subtract(n1,n2):
    return n1 - n2

# multiplication
def multiply(n1,n2):
    return n1 * n2

# dividion
def divide(n1,n2):
    return n1 / n2

operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide}

num1 = int(input("Enter the first number : "))

for symbol in operations.keys():
    print(symbol)

operation_symbol = input("Enter any one of the operations above : ")

num2 = int(input("Enter the second number : "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer} ")
