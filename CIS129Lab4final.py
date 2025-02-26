# Module 4 Lab-4
# John Miller
# 2/22/2025
# Program says how much of a bonus stores get based on there sales

#The main function

def main():

# Declaring Variables

    prompt1 = 'Enter monthly sales here: '
    prompt2 = 'Enter monthly sales increase here: '
    monthlySales = getSales(prompt1)
    salesIncrease = getIncrease(prompt2)
    storeAmount =calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount, empAmount)

    

   

# This function gets the monthly sales

def getSales(prompt1):
    monthlySales = float(input(prompt1))
    return monthlySales



    # THis function gets the percent of increase in sales 

def getIncrease(prompt2):
    salesIncrease = float(input(prompt2))
    salesIncrease = salesIncrease / 100
    return salesIncrease

    # This function determines the storeAmount bonus

def calcStoreBonus(monthlySales):

    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

    # This function determines the empAmount bonus

def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

    # This function prints the bonus information

def printBonus(storeAmount, empAmount):
    print(" The store bonus amount is $", storeAmount)
    print(" The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! you have reached the highest bonus amounts possible')



# Calls Main
main()