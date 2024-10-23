# Input:
#  price < 1.00 dollars
# Processing:
#  changeTotal (1.00 - price)
#  changeQuarters (changeTotal * .25)
#  changeDimes (changeTotal * .1)
#  changeNickels (changeTotal * .05)
#  changePennies (changeTotal * .01)
# Output:
#   changeQuarters
#   changeDimes
#   changeNickels
#   changePennies
# Math:
#  input: .5
#  Change Due: 0.5
#  Quarters: 2.0
#  Dimes: 5.0
#  Nickels: 10.0
#  Pennies: 50.0

#Get user input
price = input("Enter a price less than $1.00 but greater than 0.0 (.50): \n Amount: ")
changeTotal = 1.00 - float(price)
#Process coin data
changeQuarters = changeTotal // .25
changeDimes = changeTotal // .1
changeNickels = changeTotal // .05
changePennies = changeTotal // .01
#Display Calculations
print("Change Due: " + str(changeTotal))
print("Quarters: " + str(changeQuarters))
print("Dimes: " + str(changeDimes))
print("Nickels: " + str(changeNickels))
print("Pennies: " + str(changePennies))