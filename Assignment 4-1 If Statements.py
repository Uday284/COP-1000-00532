# Initialize variables
charge = 0.00
numChars = 18  # Change as needed for unit tests
color = "black"  # Change as needed for unit tests
woodType = "oak"  # Change as needed for unit tests

# Base charge for the sign
charge = 35.00

# Additional charge for extra characters
if numChars > 5:
    charge += (numChars - 5) * 4.00

# Additional charge for oak wood
if woodType.lower() == "oak":
    charge += 20.00

# Additional charge for gold-leaf lettering
if color.lower() == "gold":
    charge += 15.00

# Output the final charge
print(f"The charge for this sign is ${charge:.2f}")



