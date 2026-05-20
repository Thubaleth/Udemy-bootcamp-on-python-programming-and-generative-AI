

"""Store student info:

students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}

Features:

Add students
Update marks
Search students
Delete records
"""



students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}

#add students
students["103"] = {"name":"Thubalethu","marks":85}
print(students)

#update marks
students["102"]["marks"] = 95
print(students)

#search students
student_id = "102"
if student_id in students:
    print(students[student_id])
else:
    print("students not found")

#delete student
delete_student=students.pop("102")
print(students)