'''
Create a 2D array to store the marks of 3 subjects of 5 students.
Now perform the following operations on the marks array.
1. Find the maximum marks.
2. Find the minimum marks.
3. Find the average marks.
4. Find the student id(0 to 5) who scored maximum marks in subject 1.
5. Find maximum marks subject wise.
6. Find average marks subject wise.
7. Add 10 marks for all students who scored less than 50 for subject 1.
8. Find out number of students who scored more than 80 in subject 2.
9. Find out the minimum marks of student 2.
10.Find out the maximum marks of student 4.
'''

import numpy as np

marks = np.array([
    [45, 78, 85],
    [67, 82, 74],
    [39, 65, 91],
    [88, 72, 69],
    [55, 95, 80]
])

print("Maximum marks =", np.max(marks))

print("Minimum marks =", np.min(marks))

print("Average marks =", np.mean(marks))

print("Student ID with maximum marks in Subject 1 =", np.argmax(marks[:, 0]))

print("Maximum marks subject wise =", np.max(marks, axis=0))

print("Average marks subject wise =", np.mean(marks, axis=0))

marks[marks[:, 0] < 50, 0] += 10

print("Updated marks:")
print(marks)

print("Students scoring more than 80 in Subject 2 =", np.sum(marks[:, 1] > 80))

print("Minimum marks of Student 2 =", np.min(marks[1]))

print("Maximum marks of Student 4 =", np.max(marks[3]))