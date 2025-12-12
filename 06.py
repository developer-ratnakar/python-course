chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name}: {chai_type} please !")

chai_description = "Aromatic & Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reverse word: {chai_description[::-1]}")

lable_text = "Chai Special"
encoded_label = lable_text.encode("utf-8")
print(f"Non-Encoded label: {lable_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")