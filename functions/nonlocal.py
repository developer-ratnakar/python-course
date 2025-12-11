def update_kitchen():
    chai_type = "Masala"
    print(f"Original Chai Type {chai_type}")
    
    def replace_chai_type():
        nonlocal chai_type
        chai_type = "Ginger"
    replace_chai_type()
    print(f"After Replacing Chai Type {chai_type}")

update_kitchen()