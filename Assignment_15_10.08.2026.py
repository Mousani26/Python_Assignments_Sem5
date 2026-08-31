"""
Consider the given string "Python Programming" and perform the following operations on the string
•	Display "Python"
•	Display "Programming"
•	Find whether substring "java" is present or not. If not, then add "java" in between "python" and "programming".
•	Find the length of the new string.
•	Count the number of words in the string.
•	Capitalize each word in the string.
•	Remove all the spaces and print the string.
•	Print the frequency of "A", "P", "R" and "M". (Match case)
"""

text = "Python Programming"

print(text[:6])
print(text[7:])

if "java" not in text.lower():
    text = text[:6] + " java " + text[7:]

print(text)

print(len(text))

print(len(text.split()))

print(text.title())

print(text.replace(" ", ""))

print("A:", text.count("A"))
print("P:", text.count("P"))
print("R:", text.count("R"))
print("M:", text.count("M"))