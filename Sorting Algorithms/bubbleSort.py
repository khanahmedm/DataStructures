# Title: Bubblesort implementation
# Author: Ahmed M Khan
# Date Created: 6/9/21
# Date Modified: 6/9/21
# Description : Sorts a list of numbers using bubblesort algorithm

def bubbleSort(n):
    index = 0
    swap_count = 0
    for i in range(len(n)-1):
        if n[index] > n[index+1]:
            n[index], n[index+1] = n[index+1], n[index]
            swap_count += 1
        index += 1
    if swap_count > 0:
        return bubbleSort(n)
    else:
        return n

# print results 
numbers = [4,2,1,5,6,3,7,9,8]
print('orginal list:', numbers)
print('Sorted:', bubbleSort(numbers))
