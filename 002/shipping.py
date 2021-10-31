weight = 41.5
premium_shipping = 120

# Ground shipping
if weight <= 2:
    cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    cost = weight * 4 + 20
else:
    cost = weight * 4.75 + 20

print(cost)

# Premium shipping
print(premium_shipping)

# Drone shipping

if weight <= 2:
    cost = weight * 4.5
elif weight > 2 and weight <= 6:
    cost = weight * 9
elif weight > 6 and weight <= 10:
    cost = weight * 12
else:
    cost = weight * 14.25

print(cost)