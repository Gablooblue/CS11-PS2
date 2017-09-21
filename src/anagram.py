#!/bin/python3

import sys

'''
Honestly I'm not 100% sure why this program worked
but it did so who cares lmao
'''

def anagram(s):
    a = [0] * 26
    b = [0] * 26
    total = 0
    if len(s) % 2 == 1:
        return -1
    half = int(len(s) / 2)
    #Halving the strings
    s1 = s[:half]
    s2 = s[half:]

    #Counting the occurences of letters in each string
    for i in s1:
        asc = ord(i.upper()) - 65
        a[asc] += 1
    for j in s2:
        asc = ord(j.upper() ) - 65
        b[asc] += 1
        
    #Adding them up to see differences
    for i in range(26):
        a[i] = a[i] - b[i]
        #Only counting letters which need to be changed
        if a[i] > 0:
            total += a[i]
        
    return total
    
            

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
