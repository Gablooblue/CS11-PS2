#!/bin/python3

import sys

'''
Thanks Filbert for helping me with this one
I got stuck on this for the longest time 
'''

#Checking if the number is a palindrome
def checkPalindrome(n):
    n = str(n)
    for i in range(len(n)// 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True

def getProducts(n):
    m = 0 #Max
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            p = i * j #Product
            #If product is greater than n and less than max
            if(n > p > m and checkPalindrome(p)):
                m = p #Setting max to product
    return m
            
            
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = getProducts(n)
    print(x)
                
