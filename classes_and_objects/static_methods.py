class ChaiUtils:
    @staticmethod
    def cleaned_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " Water, Leaves,    Clove   , Cardamom"
cleaned = ChaiUtils.cleaned_ingredients(raw)

print(cleaned)
