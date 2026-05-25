"""
Classify student grades.

students = {
    "Alice": 85,
    "Bob": 45,
    "Charlie": 70
}

Requirements:
- Assign grades:
    A = 80+
    B = 60+
    F = below 50
- Display student grades
"""

students = {
    "Alice": 85,
    "Bob": 45,
    "Charlie": 70
}

def classify_student_grades():

 for name,mark in students.items():
  if mark >= 80:
   print(f"{name} get an A")
  elif mark >= 60 and mark < 80:
   print(f"{name} get a B")
  elif mark < 50:
   print(f"{name} get a F")

classify_student_grades()
   

