favorite_chai  = [
    "Ginger Chai", "Masala Chai", "Lemon Tea",
    "Iced Tea", "Ginger Chai", "Lemon Tea"
]

unique_chai = {chai for chai in favorite_chai if len(chai) < 10}
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cloves", "cardamom"],
    "Elaichi Chai": ["cloves", "milk"],
    "Spicy Chai": ["ginger", "cardamom", "black pepper"]
}

unique_spices = {spices for ingredients in recipes.values() for spices in ingredients}

print(unique_spices)