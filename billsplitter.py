no_of_people=int(input())
total_bill=int(input())
tip=int(input())
tip_amount=total_bill*(tip/100)
final=total_bill+tip_amount
each_person=final/no_of_people
print("Then each person have to pay:",each_person)
print(f"Tip Amount: {tip_amount}")
print(f"Final amount paid with tip: {final}")
