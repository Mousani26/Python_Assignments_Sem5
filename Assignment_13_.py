"""
13. Create a dictionary employee where employee_id is the key. The value against amp_id is a nested dictionary that in includes emp_name, designation, dept, salary. (The dictionary contains records of 5 employees) Perform the following operations on the dictionary employee.
•	Print the record of the employee with emp_id "E1".
•	Print the departmet of employee "E4".
•	Print the record of employee having maximum salary.
•	Insert a new employee record in the existing dictionary.
"""


employee = {
    "E1": {
        "emp_name": "Amit",
        "designation": "Manager",
        "dept": "HR",
        "salary": 50000
    },
    "E2": {
        "emp_name": "Rahul",
        "designation": "Developer",
        "dept": "IT",
        "salary": 60000
    },
    "E3": {
        "emp_name": "Priya",
        "designation": "Designer",
        "dept": "Design",
        "salary": 55000
    },
    "E4": {
        "emp_name": "Riya",
        "designation": "Developer",
        "dept": "IT",
        "salary": 70000
    },
    "E5": {
        "emp_name": "Ankit",
        "designation": "Accountant",
        "dept": "Finance",
        "salary": 45000
    }
}

print("Record of E1:")
print(employee["E1"])

print("\nDepartment of E4:")
print(employee["E4"]["dept"])

max_salary = 0
max_employee = ""

for emp_id in employee:
    if employee[emp_id]["salary"] > max_salary:
        max_salary = employee[emp_id]["salary"]
        max_employee = emp_id

print("\nEmployee with maximum salary:")
print(employee[max_employee])

employee["E6"] = {
    "emp_name": "Neha",
    "designation": "Tester",
    "dept": "IT",
    "salary": 52000
}

print("\nUpdated Employee Dictionary:")
print(employee)