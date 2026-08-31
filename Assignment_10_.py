'''
10. Create a list of 20 student marks and perform the following operations.
•	Find out the average marks from the list
•	Find out the number of students score more than the average in the in the list
•	Find the marks that maximum students scored in the list.
'''

marks = [78, 85, 92, 67, 85, 74, 90, 85, 69, 88,
         76, 95, 81, 85, 73, 68, 90, 85, 79, 84]

average = sum(marks) / len(marks)

print("Average marks =", average)

count = 0

for mark in marks:
    if mark > average:
        count = count + 1

print("Number of students scoring more than average =", count)

max_frequency = 0
most_scored = marks[0]

for mark in marks:
    frequency = marks.count(mark)

    if frequency > max_frequency:
        max_frequency = frequency
        most_scored = mark

print("Marks scored by maximum students =", most_scored)