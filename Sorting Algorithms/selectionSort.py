# Title: Selection sort implementation
# Author: Ahmed M Khan
# Date Created: 6/10/21
# Date Modified: 6/12/21
# Description : Sorts a list of numbers using selection sort algorithm

def selectionSort(n):
    min_index = 0
    min_val = n[min_index]
    index = 0
    for j in range(len(n)-1):
        for index in range(j, len(n)-1):
            if n[index+1] < min_val:
                min_val = n[index+1]
                min_index = index+1
        n[min_index], n[j] = n[j], n[min_index]
        min_val = n[j+1]
        min_index = j+1
    return(n)

def selectionSortv2(n):
    index = 0
    for index in range(len(n)-1):
        min_val = min(n[index:])
        min_index = n[index:].index(min_val) + index
        n[index],n[min_index] = min_val, n[index]
    return n


# print results
numbers = [10,4,2,1,5,6,3,7,9,8,1,2]
print('Without using list min and index functions')
print('Original list:', numbers)
print('Sorted list:', selectionSort(numbers))

print('Using list min and index functions')
numbers = [10,4,2,1,5,6,3,7,9,8,1,2,12,14,13]
print('Original list:', numbers)
print('Sorted list:', selectionSortv2(numbers))
