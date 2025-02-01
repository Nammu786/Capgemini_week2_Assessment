no_of_people=int(input("enter no of people:"))
total_bill=int(input("enter total bill:"))
tip=int(input("tip you wants to provide:"))
tip_amount=total_bill*(tip/100)
final=total_bill+tip_amount
each_person=final/no_of_people
print("Then each person have to pay:",each_person)
print(f"Tip Amount: {tip_amount}")
print(f"Final amount paid with tip: {final}")
