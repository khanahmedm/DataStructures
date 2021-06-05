# Title: Calculate fibonacci series
# Author: Ahmed M Khan
# Date: 6/4/21
# Description : This program calculates the next value of fibonacci series by calling the same function recursively.

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(35))
