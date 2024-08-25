"""
#
# Part : python String Formatting
#
"""

print = 60
txt = f"price is {price} baht."
print(txt)
txt = f"price is {price: .2f} baht."
print (txt)

price = 50
price = 0.25
txt = f"price is{price + (price * tax)} baht."
print(txt)

price = 1000
txt = f"price is {price:,} baht."
print(txt)