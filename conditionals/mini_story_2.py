customer_order = input("Enter Your Preffered Snack: ").lower()

cafe_products = {"cookies", "samosa"}

if customer_order in cafe_products:
    print(f"{customer_order} is available")
else:
    print(f"{customer_order} is not available")