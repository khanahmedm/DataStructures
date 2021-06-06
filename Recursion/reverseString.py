# Title: Calculates power of number
# Author: Ahmed M Khan
# Date Created: 6/5/21
# Date Modified: 6/5/21
# Description : This program calculates power of base number by multiplyig it exponent times

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])


print(reverse('recursion'))
print(reverse('australia'))
