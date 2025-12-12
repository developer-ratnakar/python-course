def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Invalid Chai Flavor")
    print(f"Brewing {flavor} chai")

brew_chai("mint")