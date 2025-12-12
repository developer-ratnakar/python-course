# Integer 

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grms of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving} litres")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot is {bags_per_pot}")

total_cadamom = 10
pods_per_cup = 3
leftpver_pods = total_cadamom % pods_per_cup
print(f"Leftover cardamom pods is {leftpver_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Powerful flavour strength is {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")