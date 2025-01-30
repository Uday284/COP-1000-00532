itemName="TV Stand"
wholesalePrice = 200.0
retailPrice = 325.0

profit = retailPrice - wholesalePrice

salePrice = retailPrice - (0.25 * retailPrice)

saleprofit = salePrice - wholesalePrice

print(f"Item Name: {itemName}")
print(f"Retail Price: ${retailPrice}")
print(f"Wholesale Price: ${wholesalePrice}")
print(f"Profit: ${profit}")
print(f"Sale price: ${salePrice}")
print(f"Sale Profit: ${saleprofit}")