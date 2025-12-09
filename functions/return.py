def chai_order(order_type):
    return order_type

return_value = chai_order("Ginger")
print(f"Return {return_value}")

chai_order("Masala")

def chai_status(cups_left):
    if cups_left == 0:
        return "Chai is Over"
    return "Chai is Ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 200, 30

cups_made, cups_left = chai_report()

print(f"Cups Made: {cups_made}")
print(f"Cups Left: {cups_left}")