weight=float(input("Enter the weight in kilograms: "))
height=float(input("enter the height in meters: "))
BMI=(weight/(height*height))
if BMI<=18.5:
    print("Underweight")
elif BMI >18.5  and BMI<24.9:
    print("Normal")
elif BMI>25.0 and BMI< 29.9:
    print("OverWeight")
else:
    print("obesity")    