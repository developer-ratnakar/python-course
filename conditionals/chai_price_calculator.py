small_tea_price = 10
medium_tea_price = 15
large_tea_price = 20

tea_size_customer_wants = input("Enter Your Preffered Tea Size(small, medium, large): ")

if tea_size_customer_wants == "small":
    print(f"Price is {small_tea_price}")
elif tea_size_customer_wants == "medium":
    print(f"Price is {medium_tea_price}")
elif tea_size_customer_wants == "large":
    print(f"Price is {large_tea_price}")
else:
    print("Unknown Cup")

