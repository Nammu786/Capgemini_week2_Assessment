
while True:
    def add_items(item_name,price):
            print(" Go add more products!!")
    item_name=input("Enter the item name: ")
    price=int(input("enter the price of item: "))
    add_items(item_name,price)
    str1=input("exit/stay")      
    if str1=="exit":
        break
    Tprice=0
    Tprice=Tprice+price
    print(Tprice)
def view_cart():
    print(f"item_name :{item_name} and cost of the item is {price}")
    add_items(item_name,price)
view_cart()


    