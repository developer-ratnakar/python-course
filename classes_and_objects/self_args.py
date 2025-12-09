class ChaiCup:
    cup_size = 100 #ml

    def describe(self):
        return f"A Cup of size is {self.cup_size}ml"


result = ChaiCup()
print(result.describe())
print(ChaiCup.describe(result))