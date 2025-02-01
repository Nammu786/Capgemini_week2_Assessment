'''17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. 
Implement this in `SQLDatabase` and `NoSQLDatabase`.'''

from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    details={"name":"namratha","age":"20"}
    def insert(self):
        print("Operations in SQL database")
        self.details["id"]=1238
        print(f"student details:{self.details}")
    def update(self):
        self.details["age"]=30
        print(f"Updated details:",self.details)
    def delete(self):
        del self.details["name"]
        print("After deletion:",self.details)

class NOSQLDatabase(IDatabaseOperations):
    details={"name":"srujana","age":"21"}
    def insert(self):
        print()
        print("Operations in NOSQL database")
        self.details["id"]=1221
        print(f"student details:{self.details} ")
    def update(self):
        self.details["name"]="harshini"
        print(f"Updated details:",self.details)
    def delete(self):
        del self.details["name"]
        print("After delection:",self.details)
sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql=NOSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()
            