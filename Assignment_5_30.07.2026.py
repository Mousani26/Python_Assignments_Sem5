#Write a python program to define a method isPrime with a parameter num to check whether num is prime or not.

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if isPrime(num):
    print("The number is prime.")
else:
    print("The number is not prime.")