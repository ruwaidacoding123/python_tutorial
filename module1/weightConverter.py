# Get the weight from user input and convert it to a float
weight = float(input('Weight: '))

# Get the unit type from user input
unit = input('(L)bs or (K)g: ')

# Convert the weight based on the unit
if unit.upper() == "L":
    # Convert pounds to kilograms
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    # Convert kilograms to pounds
    converted = weight / 0.45
    print(f"You are {converted} pounds")
