#Create a class Student with attributes name, dept, roll. Initialize the attribute with the constructor. Display the record of student using show(). Define 5 student objects and show records of 5 students.

class Student:
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Roll No:", self.roll)
        print()


student1 = Student("Amit", "CSE", 101)
student2 = Student("Rahul", "CSE", 102)
student3 = Student("Priya", "IT", 103)
student4 = Student("Riya", "CSE", 104)
student5 = Student("Ankit", "ECE", 105)


print("Student 1:")
student1.show()

print("Student 2:")
student2.show()

print("Student 3:")
student3.show()

print("Student 4:")
student4.show()

print("Student 5:")
student5.show()