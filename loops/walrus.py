value = 13

if(remainder := value % 5):
    print(f"Not divisible by 5. Remainder: {remainder}")

available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your preffered size: ").lower()) in available_sizes:
    print(f"{requested_size} is available")
else:
    print(f"{requested_size} is available")

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available Flavors: ", flavors)

while(flavor := input("Choose any flavor: ".lower())) not in flavors:
    print(f"{flavor} is unavailable")

print(f"You choose {flavor}")
