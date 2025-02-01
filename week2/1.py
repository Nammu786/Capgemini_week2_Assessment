'''Class and Object
•	1. Create a class `Employee` with properties `name`, `id`, and `department`.
       Instantiate an object and assign values dynamically.
'''

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def person(self):
        print(f"\nEmployee name:{self.name}\nId:{self.id}\nDepartment:{self.department}")
e=Employee(input("Enter name:"),int(input("Enter Id:")),input("Enter Department:"))
e.person()




