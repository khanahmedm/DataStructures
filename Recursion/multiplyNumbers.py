# Title: Calculates the product of list of numbers
# Author: Ahmed M Khan
# Date Created: 6/6/21
# Date Modified: 6/6/21
# Description : This program multiplies all the numbers in a list

def multiply(l):
    if len(l) == 0:
        return 1
    else:
        return l[0] * multiply(l[1:])




print(multiply([1,2,3])) #6
print(multiply([2,3,4])) #24
print(multiply([3,4,5])) #60
