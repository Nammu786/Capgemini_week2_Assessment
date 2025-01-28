cart={"maxi":450,"tshirt":200,"shirt":600,"frock":800}
def add_items(item_name,price):
    if item_name in cart:
        cart[item_name]+=price
    else:
        cart[item_name]=price
    print(f'{item_name} added to the cart with price {price}')
def view_cart():
    if not cart:
        print("empty")
    else:
        print("the items in the cart are",cart.items()) 
view_cart()   
def total():
    total=sum(cart.values())
    print("total amount:",total)
total()
    

    