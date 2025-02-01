
''' 4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`.
      Write a method to return student details.'''

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def student_details(self):
        print(f'Student name: {self.name}\nRollno: {self.roll_number}')
student=Student("namratha",1238)
student.student_details()

student=Student("srujana",1224)
student.student_details()

student=Student("harshini",1221)
student.student_details()