base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Full Mix {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong Brew {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw Spice Data {raw_spice_data}")