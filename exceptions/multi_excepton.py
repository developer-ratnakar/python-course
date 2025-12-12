def process_order(item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print("Total cost is: ", cost)
    except KeyError as k:
        print("Sorry That Chai is not in the menu")
    except TypeError as v:
        print("The Quantity Must be a Integer")

process_order("Masala", 4)
process_order("Ginger", 4)
process_order("Masala", "Masala")