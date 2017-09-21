#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

for c in s:
    curr = ord(c)
    r = True
    #If the string contains lowercase letters
    if 97 <= ord(c) <= 122:
        low = 97
        high = 122
    #if the string contains uppercase letters
    elif 65 <= ord(c) <= 90:
        low = 65
        high = 90
    #if the character is not a letter
    else: 
        low = 0
        high = 0
        r = False

    for i in range(k):
        if r:
            if curr == high:
                curr = low 
            else:
                curr += 1
    print(chr(curr), end = "")
