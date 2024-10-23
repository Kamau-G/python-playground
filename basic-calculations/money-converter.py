# Input: USDollar
# Processing: Exchange rate in Euros, Canadian, Pesos
# Output: convertedEuros, convertedCanadian, convertedPesos
#
# 100USD * .93  = 93EUR
# 100USD * 19.07  = 1907MXN
# 100USD * 1.34  = 134CAD
#
print("Enter a US dollar amount to see its exchange rate (100)")
usDollar = int(input("Amount: "))
convertedEuros = usDollar * .93
convertedPesos = usDollar * 19.07
convertedCanadian = usDollar * 1.34
print("Euros: " + str(convertedEuros))
print("Pesos: " + str(convertedPesos))
print("Canadian Dollars: " + str(convertedCanadian))