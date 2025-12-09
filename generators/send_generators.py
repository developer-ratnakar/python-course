def chai_customer():
    print("Welcome! What Chai You Want to Order ?")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield

stall = chai_customer()

next(stall)

stall.send("Masala Chai")
stall.send("Ginger Chai")