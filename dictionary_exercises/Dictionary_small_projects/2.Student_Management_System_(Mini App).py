"""Create a system that stores student data:

students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}

Requirements:
- Create a function to add a student
- Create a function to update marks
- Create a function to search for a student by ID
- Create a function to delete a student
- Create a function to display all students
- Use a loop to create a menu system
"""

students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}

# Add student
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    students[student_id] = {"name": name, "marks": marks}
    print("Student added successfully!")

# Update marks
def update_marks():
    student_id = input("Enter student ID to update: ")

    if student_id in students:
        marks = int(input("Enter new marks: "))
        students[student_id]["marks"] = marks
        print("Marks updated!")
    else:
        print("Student not found!")

# Search student
def student_search():
    student_id = input("Enter student ID: ")

    if student_id in students:
        print(students[student_id])
    else:
        print("No student found!")

# Delete student
def delete_student():
    student_id = input("Enter student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted!")
    else:
        print("Student not found!")

# Display all students
def display_all_students():
    if students:
        for student_id, info in students.items():
            print(student_id, info)
    else:
        print("No records found!")

# Menu system
def menu_system():
    while True:
        num = int(input(
            "\n1. Add student\n"
            "2. Update marks\n"
            "3. Search student\n"
            "4. Delete student\n"
            "5. Display all students\n"
            "6. Exit\n"
            "Enter your choice: "
        ))

        if num == 1:
            add_student()

        elif num == 2:
            update_marks()

        elif num == 3:
            student_search()

        elif num == 4:
            delete_student()

        elif num == 5:
            display_all_students()

        elif num == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

# Run program
menu_system()



