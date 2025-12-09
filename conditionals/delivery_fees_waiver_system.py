delivery_amount = 30
order_amount  = input("Enter Order Amount: ")

delivery_amount == 0 if int(order_amount) > 300 else delivery_amount == 30

print(f"Deliver is Free") if int(order_amount) > 300 else print("Delivery Amount is 30")
