# The Shopping Cart

item = input("Enter the item to Buy: ")
quantity = int(input("Enter the Quantity :"))
price =  float(input(f"price for {item} is :"))

total = quantity *  price

print(f"You have Brought  : {quantity}/ {item}  ")
print(f"Your Total is {round(total, 2)}")