staff = [("Sudipta", 5), ("Bikash", 34), ("Srikanta", "65")]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage staff")
        break

else:
    print("No one is eligible to manage staff")