class Student:
  def __init__(self, name, roll_number, cgba):
    self.name = name
    self.roll_number = roll_number
    self.cgba = cgba

def sort_students(student_list):
  sorted_students= sorted(student_list, key=lambda student: student.cgba,reverse=True)
  return sorted_students

students =[
 Student("Hajira","101",8.2),
 Student("Raji","102",8.4),
 Student("Jenifer","103",9.6),
 Student("Prabha","104",9.7)
]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name:{}, Roll_Number:{},CGBA:{}".format(student.name,student.roll_number,student.cgba))