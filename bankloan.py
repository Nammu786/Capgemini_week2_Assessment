name=input("enter name:")
age=int(input("enter age: "))
salary=int(input("enter salary amount:"))
credit_score=float(input("enter cibil score:"))
print("Thank you! For applying the Loan:")
if age>=18 and salary>30000 and credit_score>=750: 
    print("Loan Approved") 
else:      
    if credit_score<750:
        print("Loan Rejected,due to Low cibil score")
    if age<=18:
        print("Loan Rejected,Due to underage")
    if salary<=30000:
        print("Loan Rejected,Due to Less income")    
       