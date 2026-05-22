
"""Analyze student marks.

students = {
    "Alice": [80, 90, 85],
    "Bob": [60, 70, 65]
}

Requirements:
- Calculate average marks
- Find top student
- Find students below 50
- Display class statistics
"""

students = {
    "Alice": [80, 90, 85],
    "Bob": [60, 70, 65],
    "ray":[10,20,30]
}

def Analyze_student_marks():

    name = input("Enter the student name: ")
    sum = 0
    for mark in students[name]:
        sum += mark
    
    avg = sum/len(students[name])
        
    return avg



#Find top student
def top_students():
    
    for name,marks in students.items():
        avg = sum(marks) / len(marks)
    
    
    
        top_avg = 0
        top_students = ""
    
        if avg > top_avg:
         top_avg = avg
         top_students =name
        
    return f"the top student is {top_students} with the average marks of {top_avg}"


         
       
    
#Find students below 50
def students_below_50():
   low_students = []
   for name,marks in students.items():
      avg = sum(marks) / len(marks)

      if avg < 50:
         low_students.append(name)
       
   return " ".join(low_students)


#Display class statistics


    









