# Title: Find first capital letter in a string
# Author: Ahmed M Khan
# Date Created: 6/9/21
# Date Modified: 6/9/21
# Description : This program finds first occurence of capital letter in a string

def firstCapital(s):
    if len(s) < 1:
        return 'no capital letter found'
    elif s[0].isupper():
        return s[0]
    else:
        return firstCapital(s[1:])

words = ['Sam', 'sAm', 'saM', 'geeKs', 'gEeKs']
# print results
for word in words:
    print('First capital letter in',word,' is:', firstCapital(word))
