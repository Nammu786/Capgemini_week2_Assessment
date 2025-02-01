'''	7. Create a multi-level class structure 
with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.'''

class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Iam {self.name} jobless person now")
class Employee(Person):
    def __init__(self, name,company_name,shift_type,id):
        super().__init__(name)
        self.company_name=company_name
        self.shift_type=shift_type
        self.id=id
    def show1(self):
        print(f"Iam a employee now, details are: name:{self.name}\n company name:{self.company_name}\nid:{self.id}\n Type of shift(day/night):{self.shift_type} ")
        print()
class Manager(Employee):
    def __init__(self, name, company_name, shift_type, id,salary,position):
        super().__init__(name, company_name, shift_type, id)
        self.position=position
        self.salary=salary
    def manager_deatils(self):
        print(f"Manager details are:\n name:{self.name}\n company name:{self.company_name}\nid:{self.id}\n Type of shift(day/night):{self.shift_type}\n position:{self.position}\nsalary:{self.salary}")   
        print()
    def approve_leave(self):
        print("Your leave approved")

e=Employee("alice","Accenture",'day',1221)
e.show1()

manager=Manager('namratha','Capg',"Day",1238,35000,"Manager")
manager.manager_deatils()
manager.approve_leave()