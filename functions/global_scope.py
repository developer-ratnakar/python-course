chai_type = "Ginger"

def update_kitchen():
    def kitchen():
        global chai_type
        chai_type = "Masala"
    kitchen()

update_kitchen()
print(f"Chai Type: {chai_type}")