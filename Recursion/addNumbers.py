# Title: Calculates sum of numbers in a list
# Author: Ahmed M Khan
# Date Created: 6/8/21
# Date Modified: 6/8/21
# Description : This program adds up all the numbers in a list

def add(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + add(l[1:])

# print results
print(add([1,2,3])) #6
print(add([2,3,4])) #9
print(add([3,4,5])) #12
