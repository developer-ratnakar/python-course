ingrediants  = ["water", "milk", "black tea"]
ingrediants.append("sugar")
print(f"Ingrediants are: {ingrediants}")

ingrediants.remove("water")
print(f"Ingrediants are: {ingrediants}")

spice_options = ["ginger", "cardamom"]
chai_ingrediants = ["water", "milk"]

chai_ingrediants.extend(spice_options)
print(f"chai: {chai_ingrediants}" )

chai_ingrediants.insert(2, 'black tea')
print(f"after insert chai: {chai_ingrediants}" )

last_added = chai_ingrediants.pop()
print(f"after pop chai: {chai_ingrediants}, last added: {last_added}" )

chai_ingrediants.reverse()
print(f"after reverse chai: {chai_ingrediants}" )

chai_ingrediants.sort()
print(f"after sorting chai: {chai_ingrediants}" )

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")