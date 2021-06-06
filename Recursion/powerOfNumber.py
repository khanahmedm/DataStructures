# Title: Calculates power of number
# Author: Ahmed M Khan
# Date Created: 6/5/21
# Date Modified: 6/5/21
# Description : This program calculates power of base number by multiplyig it exponent times

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

print(power(3,0))
print(power(3,1))
print(power(3,2))
print(power(3,3))
