#The purpose of this code is to calculate the result of raising a number to a specified power based on user input

import math

# store user input for number and power
number = int(input("please enter base number: "))
power = int(input("please enter power: "))


# use pow function from math module
result = math.pow(number, power)

print(result)