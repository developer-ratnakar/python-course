flavors = ["Ginger", "Out Of Stock", "Tulsi", "Discontinued", "Masala"]

for flavor in flavors:
    if flavor == "Out Of Stock":
        continue
    elif flavor == "Discontinued":
        break
    print(f"Serving Chai with {flavor}")

print("Outside of the loop")