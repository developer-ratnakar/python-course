chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order {chai_order}")

chai_reciepe = {}
chai_reciepe["base"] = "black tea"
chai_reciepe["liquid"] = "milk"

print(f"Recipe: {chai_reciepe['base']}")

del chai_reciepe["liquid"]
print(f"Recipe: {chai_reciepe}")

print(f"Is Sugar Available in Chai Order ? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar":1}
print(f"Chai Order (keys): {chai_order.keys()}")
print(f"Chai Order (values): {chai_order.values()}")
print(f"Chai Order (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last Item: {last_item}")

extra_spices = {"cardamom": "crushed", "cinnamon": "mixed"}
chai_reciepe.update(extra_spices)
print(f"Updated Chai Reciepe: {chai_reciepe}")

chai_size = chai_order["size"]
print(f"Chai Size: {chai_size}")

customer_note = chai_order.get("note", "no note")
print(f"customer_note: {customer_note}")