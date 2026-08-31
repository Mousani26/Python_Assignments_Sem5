"""
Write a python program to implement following funtions:
•	Lambda (lambda function is anonymous function)
•	Filter
•	Map
"""

numbers = [1, 2, 3, 4, 5, 6]

square = lambda x: x * x
print("Lambda:", square(5))

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter:", even)

squares = list(map(lambda x: x * x, numbers))
print("Map:", squares)