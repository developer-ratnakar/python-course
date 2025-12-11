class Chai:
    temperature = "Hot"
    strength = "Strong"


cutting  = Chai()

cutting.temperature = "Mild"

print(cutting.temperature)

del cutting.temperature

print(cutting.temperature)