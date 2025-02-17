# Input of products (how many coffees/ muffins)

Mycoffee = int(input('how many coffees would you like?: '))
Mymuffin = int(input('how many muffins would you like?: '))

# Math for Costs
coffeeCost = 5*Mycoffee
muffinCost = 4*Mymuffin

total =float(coffeeCost + muffinCost)
tax = 0.06*total
total2 = tax + total

# * lines for receipt format
line_length = 40
secondline_length = 10

# Input Receipt Formatting

print('*' * line_length)
print('My Coffee and Muffin Shop\n Number of coffees bought?\n', Mycoffee)
print('Number of muffins bought?\n', Mymuffin)
print('*' * line_length)
print('*' * line_length)

# Output Receipt Formatting

print('My Coffee and Muffin Shop Receipt')
print(Mycoffee, "Coffee at $5 each:", "$%0.2f" % coffeeCost)
print(Mymuffin, "Muffins at $4 each: ", "$%0.2f" % muffinCost)
print("6% tax: ", "$%0.2f" % tax)

# Printing Total

print("-" * secondline_length)
print('Total:', "$%0.2f" % total2)