class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        return f"Preparing {self.type} Chai...."

# inheritance

class MasalaChai(BaseChai):
    def add_spices(self):
        return "Added some cardamom, cloves, ginger"

# compositions

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Masala")

    def serve(self):
        return f"Serving {self.chai.type} Chai in the shop"
        self.chai.prepare()

class FancyShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyShop()

print(shop.serve())
print(fancy.serve())

print(fancy.chai.add_spices())

