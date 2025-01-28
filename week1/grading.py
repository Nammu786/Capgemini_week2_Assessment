student_name=input("Enter student name:")
telugu=int(input("enter telugu marks:"))
hindi=int(input("enter hindi marks: "))
english=int(input("enter english marks:"))
maths=int(input("enter maths marks:"))
science=int(input("enter science marks:"))
Total_marks=telugu+hindi+english+maths+science
print(f'Total_marks of student {student_name} is {Total_marks}')
percentage=(Total_marks/500)*100 
print(f'Overall Percentage of {student_name} is {percentage}')
if percentage >=89 and percentage<=100:
    print("The Grade is A")
elif percentage>=79 and percentage<89:
    print("The Grade is B")
elif percentage>=69 and percentage<79:
    print("The Grade is C")    
elif percentage>=59 and percentage<69:
    print("The Grade is D")
else:
    print("Fail!! ")        