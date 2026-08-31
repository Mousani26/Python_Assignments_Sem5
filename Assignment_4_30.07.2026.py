#Write a python program to define a method factorial that takes one parameter and returns the result after computing the factorial of the given number.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial =", result)