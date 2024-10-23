# fahrenheit converter
# Input:
#  tempFahrenheit
# Processing:
#  Calculate tempCelsius
# Output:
#  Print tempCelsius
#
# Math:
# celsius = 5/9 * (fahrenheit - 32)
# If fahrenheit = 50 Celsius = 10
# 10 = 5/9 * (50 - 30)

tempFahrenheit = int(input("<<Welcome to fahrenheit to celsius script>>\n Enter degrees in fahrenheit: \n"))
tempCelsius = 5/9 * (tempFahrenheit - 32)
print(str(tempFahrenheit) + " degrees fahrenheit converted to celsius equals " + str(tempCelsius) + " degrees celsius")