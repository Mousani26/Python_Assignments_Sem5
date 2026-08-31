#Write a python program to define a method dosum with a parameter num to find out the sum of the digit of the num and return it.

def doSum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    return sum


num = int(input("Enter a number: "))

result = doSum(num)

print("Sum of digits =", result)