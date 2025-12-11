isDeviceOn = True
temp_of_device = 32

if isDeviceOn and temp_of_device > 35:
    print(f"Warning! Device Temperature is {temp_of_device}")
elif isDeviceOn and temp_of_device <= 35:
    print(f"Device Temperature is {temp_of_device}")
else:
    print("Device is off")