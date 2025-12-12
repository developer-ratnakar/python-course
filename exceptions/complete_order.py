class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That Chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of Cups Must be in Integer")

        total = menu[flavor] * cups
        print(f"Your bill for {cups} of {flavor} chai: rupees {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thankyou for visiting chaicode!")

bill("mint", 2)
bill("masala", "Three")
bill("ginger", 3)