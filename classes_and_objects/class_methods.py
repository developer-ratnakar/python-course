class Chai:
    def __init__(self, chai_type, strength, flavor):
        self.chai_type = chai_type
        self.strength = strength
        self.flavor = flavor

    @classmethod
    def from_dict(cls, chai_order):
        return cls (
            chai_order["chai_type"],
            chai_order["strength"],
            chai_order["flavor"]
        )

    @classmethod
    def from_string(cls, chai_string):
        chai_type, strength, flavor = chai_string.split("-")
        return cls(chai_type, strength, flavor)


order1 = Chai.from_dict({
    "chai_type": "Ginger",
    "strength": "Medium",
    "flavor": "Sweet"
})

order2 = Chai.from_string("Masala-Medium-Sweet")

print(order1.__dict__)
print(order2.__dict__)