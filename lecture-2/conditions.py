from math import modf 

number = float(input("Enter a number: "))
isEven = number % 2 == 0
isFractional = modf(number)[0] > 0

print(f"\nFacts about:\t{number}\nEven:\t\t{isEven}\n\
Fractional: \t{isFractional}\nAND...")

if number > 0:
    print("It is greater than zero")
elif number == 0:
    print("It is equal to zero")
else:
    print("It is less than zero")

