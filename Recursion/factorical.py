# Title: Calculate factorials
# Author: Ahmed M Khan
# Date: 6/4/21
# Description : This program calculates factorials by calling the same function recursively

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
