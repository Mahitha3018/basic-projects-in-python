print("--------------SUPER MARKET BILLING SYSTEM--------------")
# Taking inputs of items from the user
item_name=input("Name of the item")
item_quantity=int(input("Quantity"))
item_price=float(input("Price of the item"))
tax_percentage=float(input("Tax percentage"))
# calculating the price of the item without tax
total_price=item_quantity*item_price
#calculating tax
tax=(total_price*tax_percentage)/100
# calculating final amount
final_amount=tax+total_price
print("--------------BILL DETAILS--------------")
print("Name of the item:", item_name)
print("Quantity:", item_quantity)
print("Price of the item:", item_price)
print("Total price without tax:", total_price)
print("Tax amount:", tax)
print("Finalprice:",final_amount)
print("THANK YOU\nGLAD TO SEE YOU SOON!!!")