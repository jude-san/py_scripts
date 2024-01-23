
user = float(input("Charge for food: "))

tax = 3.50
print("Sales tax: {}".format(tax))
tip = 9.00
print("Tip: {}".format(tip))

cal = user * tax + tip

print("Grand total: {}".format(cal))