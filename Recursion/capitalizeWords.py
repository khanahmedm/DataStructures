# Title: Convert all letters to capital letters
# Author: Ahmed M Khan
# Date Created: 6/5/21
# Date Modified: 6/5/21
# Description : This program capitalizes all letters of words in a list

def capitalizeWords(l2):
    result = []
    if len(l2) == 0:
        return result
    else:
        result.append(l2[0].upper())
        return result + capitalizeWords(l2[1:])

l =  ['recursion', 'is', 'fun', 'to', 'learn']

print('original list:', l)
print(capitalizeWords(l))
