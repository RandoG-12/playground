import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Only integers are supported.")
    sys.exit()

try:
    result = x / y
except ZeroDivisionError:
    print("Division by zero is not supported.")
    sys.exit()

print(f"{x}/{y} = {result}")
    
