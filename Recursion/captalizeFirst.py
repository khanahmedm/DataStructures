# Title: Capitalize first letter
# Author: Ahmed M Khan
# Date: 6/4/21
# Description : This program capitalizes the first letter in every word in the list.

def capitalizeFirst(l2):
    result = []
    if len(l2) == 0:
        return result
    else:
        result.append(l2[0][0].upper() + l2[0][1:])
        return result + capitalizeFirst(l2[1:])

l = ['truck', 'ship', 'mountain']

print(capitalizeFirst(l))
