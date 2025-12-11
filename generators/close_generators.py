def inter_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Oolong"

def full_menu():
    yield from inter_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting For Order"
    except:
        print("Shop is closed now!")

stall = chai_stall()
print(next(stall))
stall.close()