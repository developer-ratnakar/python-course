class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summery(self):
        return f"You ordered a {self.type} chai of {self.size}ml"

chai_order = ChaiOrder("Masala", 200)
print(chai_order.summery())