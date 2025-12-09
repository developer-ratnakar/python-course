class Chai:
    source = "India"

print(Chai.source)

Chai.is_hot = True
print(Chai.is_hot)

# creating object

masala = Chai()
print(masala.source)

masala.flavor = "Ginger"
print(masala.flavor)

Chai.flavor = "Lemon"

print(Chai.flavor)
print(masala.flavor)