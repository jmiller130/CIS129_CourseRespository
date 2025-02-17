# Input of products (how many coffees/ muffins)

myCoffee = int(input('how many coffees would you like?: '))
myMuffin = int(input('how many muffins would you like?: '))
myScone = int(input('how many scones would you like?: '))
myTea = int(input('how many teas would you like?: '))


# Math for Costs of products

coffeeCost = 5*myCoffee
muffinCost = 4*myMuffin
sconeCost = 3*myScone
teaCost = 2*myTea

#Calculations for Tax and Total of Products

total = float(coffeeCost + muffinCost + sconeCost + teaCost)
tax = 0.06*total
total2 = tax + total

# * lines for receipt format

line_length = 40
secondline_length = 10

# Break Line of *

print('*' * line_length)

#Input Receipt Formatting

print('My Coffee and Muffin Shop\n Number of coffees bought?\n', myCoffee)
print('Number of muffins bought?\n', myMuffin)
print('Number of scones bought?\n', myScone)
print('Number of teas bought?\n', myTea)

#Line breaks in Receipt of *

print('*' * line_length)
print('*' * line_length)

# Output Receipt Formatting

print('My Coffee and Muffin Shop Receipt')
print(myCoffee, "Coffee at $5 each:", "$%0.2f" % coffeeCost)
print(myMuffin, "Muffins at $4 each:", "$%0.2f" % muffinCost)
print(myScone, 'Scones at $3 each:', "$%0.2f" % sconeCost)
print(myTea, 'Teas at $2 each:', "$%0.2f" % teaCost)
print("6% tax: ", "$%0.2f" % tax)

# Printing Total

print("-" * secondline_length)
print('Total:', "$%0.2f" % total2)

#Prints Final Break Line and Message

print('*' * line_length)
print('Thank you for choosing My Coffee and Muffin Shop\n We look forward to seeing you again soon')
