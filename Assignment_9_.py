'''
8. Create a list of 10 student name and another list of their marks.
Find out the students having maximum and minimum marks. 
(Both of the lists are unsorted and should not have any duplicate values.)
'''

names = ["Amit", "Rahul", "Priya", "Riya", "Ankit",
         "Neha", "Karan", "Suman", "Pooja", "Arjun"]

marks = [78, 92, 65, 88, 55, 95, 72, 60, 85, 70]

max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Student with maximum marks:", names[max_index])
print("Maximum marks:", max_marks)

print("Student with minimum marks:", names[min_index])
print("Minimum marks:", min_marks)