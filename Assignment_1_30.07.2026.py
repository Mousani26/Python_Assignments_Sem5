#Assignment 1
#Write a python program to create a calculator that will take two numbers from user and perform the following operations : Addition, Subtraction, Multiplication, Division.

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operand = int(input("choose an operand :"))

if operand == 1 :
    print("Addition = ", num1 + num2)

elif operand == 2:
    print("Subtraction = ", num1 - num2)

elif operand == 3:
    print("Multiplication = ", num1 * num2)

elif operand == 4:
    if num2 != 0:
        print("Division = ", num1/num2)
    else:
        print("cannot divide by zero")

else:
    print("invalid choice")