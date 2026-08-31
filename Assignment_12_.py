"""
12. Create set fruits having 10 fruits and create another set “summer_fruits” of fruits that are only available in summer season, “winter_fruits” of 5 fruits of fruits only grow winter season. Perform the following operations on these sets.
•	Print the name of all fruits in 3 sets.
•	Print the name of fruits that are present both in fruits and winter_fruits.
•	Print the name of the fruits that are present only in summer_fruits but not in fruits.
•	Print the name of the fruits present in summer_fruits and winter_fruits but not in fruits.
•	Find whether "orange" is present in fruits or not.
•	Find in which set "Pineapple" is present.
"""

fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes",
          "Guava", "Papaya", "Pineapple", "Watermelon", "Strawberry"}

summer_fruits = {"Mango", "Watermelon", "Litchi", "Pineapple", "Muskmelon"}

winter_fruits = {"Orange", "Apple", "Guava", "Strawberry", "Kiwi"}

print("Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)

print("\nFruits present in both fruits and winter_fruits:")
print(fruits & winter_fruits)

print("\nFruits present only in summer_fruits but not in fruits:")
print(summer_fruits - fruits)

print("\nFruits present in summer_fruits and winter_fruits but not in fruits:")
print((summer_fruits & winter_fruits) - fruits)

print("\nIs Orange present in fruits?")
if "Orange" in fruits:
    print("Yes")
else:
    print("No")

print("\nPineapple is present in:")
if "Pineapple" in fruits:
    print("fruits")

if "Pineapple" in summer_fruits:
    print("summer_fruits")

if "Pineapple" in winter_fruits:
    print("winter_fruits")