def pour_chai(n):
    print(n)
    if n == 0:
        return "All the chais are poured"
    return pour_chai(n-1)

print(pour_chai(3))

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_tea = list(filter(lambda chai: chai != "kadak", chai_types))

print(strong_tea)