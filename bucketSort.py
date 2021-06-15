# Title: Bucket sort implementation
# Author: Ahmed M Khan
# Date Created: 6/14/21
# Date Modified: 6/14/21
# Description : Sorts a list of numbers using bucket sort algorithm

import math
#from insertionSort import insertionSort
import insertionSort as sort

def bucketSort(n):
    bucket = 0
    maxValue = max(n)
    numOfBuckets = round(math.sqrt(len(n)))
    buckets = [[] for i in range(numOfBuckets)]
    sorted = []

    for i in range(numOfBuckets):
        for j in range(len(n)):
            bucket = math.ceil(n[j]*numOfBuckets/maxValue)-1
            if n[j] not in buckets[bucket]:
                buckets[bucket].append(n[j])

    for i in range(numOfBuckets):
        buckets[i] = sort.insertionSort(buckets[i])
        sorted = sorted + buckets[i]

    return sorted


# print results
numbers = [4,2,1,5,3,8,10,7,9,6]
print('Original list:', numbers)
print('Sorted list:', bucketSort(numbers))
