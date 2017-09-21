'''
A function to get the factorial of a number
@params number n
@returns factorial
'''
def factorial(n):
    i = 1
    for j in range(1, n+ 1):
        i *= j
    return i

x = int(input())

e = 0
for n in range(100):
        e += x**n / factorial(n)
    
e = round(e, 10)

#To make sure it always prints 10 decimals
print("%.10f" % e)
