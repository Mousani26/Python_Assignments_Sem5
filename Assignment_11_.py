"""
11. Create a tuple of 20 employee name. Perform the following operation on the tuple:
•	Print each name and frequency of that name in the tuple.
•	Remove the duplicate items from the tuple and find the number of distinct name in the tuple.
•	Print the name of the employee having maximum frequency.
•	Sort the tuple in alphabetical order and display.
•	Input a specific employee name and find whether that name exist in the tuple or not.
"""
employees = (
    "Amit", "Rahul", "Priya", "Amit", "Riya",
    "Rahul", "Suman", "Ankit", "Priya", "Amit",
    "Neha", "Riya", "Rahul", "Karan", "Ankit",
    "Amit", "Suman", "Rahul", "Neha", "Amit"
)

print("Name and Frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))

distinct_names = tuple(set(employees))

print("\nTuple after removing duplicates:")
print(distinct_names)

print("Number of distinct names:", len(distinct_names))

max_frequency = 0
max_name = ""

for name in set(employees):
    frequency = employees.count(name)

    if frequency > max_frequency:
        max_frequency = frequency
        max_name = name

print("\nEmployee with maximum frequency:", max_name)
print("Frequency:", max_frequency)

sorted_employees = tuple(sorted(employees))

print("\nTuple in alphabetical order:")
print(sorted_employees)

search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")