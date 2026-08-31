#Write a python program to define a method check_armstrong with a parameter num that will return True if the number is Armstrong else False.

def checkArmstrong(num):
    original = num
    sum = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if checkArmstrong(num):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")