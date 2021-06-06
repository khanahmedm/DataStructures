# Title: Check for palindrome in a number
# Author: Ahmed M Khan
# Date Created: 6/6/21
# Date Modified: 6/6/21
# Description : This program checks for palidrome in a number

def PalinNum(l):
    if len(l) == 0:
        return True
    elif l[0] == l[-1]:
        return PalinNum(l[1:-1])
    else:
        return False

# passing a number as string to function PalinNum
# print results
print(PalinNum(str(11311)))
print(PalinNum(str(113111)))
