# Title: Check for palindrome
# Author: Ahmed M Khan
# Date Created: 6/5/21
# Date Modified: 6/5/21
# Description : This program checks for palidrome in a string

def isPalindrome(s):
    if len(s) == 0:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

# list of words
words = ['kayak', 'deed', 'racingcar', 'racecar', 'steponnopets']

# print results
for word in words:
    print('word:', word, '\tIs palindrome:', isPalindrome(word))
