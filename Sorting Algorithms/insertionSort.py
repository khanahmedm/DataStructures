# Title: Insertion sort implementation
# Author: Ahmed M Khan
# Date Created: 6/13/21
# Date Modified: 6/13/21
# Description : Sorts a list of numbers using insertion sort algorithm

def insertionSort(n):
    index_key = 0
    for i in range(len(n)-1):
        key = n[i+1]
        for j in range(len(n[:i+1]),-1,-1):
            if key < n[j]:
                n[j+1] = n[j]
                index_key = j
        n[index_key] = key
    return n

# print results
numbers = [10,4,2,1,5,3,8,7,9,6]
print('Original list:', numbers)
print('Sorted list:', insertionSort(numbers))
