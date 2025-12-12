chai_menu = {"masala": 30, "ginger": 40}

try:
    masala = chai_menu["masala"]
except KeyError:
    print("The Key You are expecting to find is not present in the dictionary")