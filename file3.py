
''' 3. Write a python program that calculates the factorial of a given number.'''

def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f - 1)


num = int(input("Enter  number: "))


if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))
