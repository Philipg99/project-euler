'''
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
from time import time as t
t1 = t()
#solving by going through all terms
a,b,sum = 1,1,0
while (b < 4000000):
    a,b = b,a+b
    if b%2 == 0:
        sum += b
print(sum)
#
t1 = t() - t1
print (t1*10**10)

t2 = t()
#solving by iterating through every third element
a,b,sum = 1,2,0
while (b < 4000000):
    if b%2 == 0:
        sum += b
    a = a + b
    b = a + b
    a,b = b,a+b
print(sum)
#
t2 = t() - t2
print (t2*10**10)

if t2>t1:
    print('First is faster')
else:
    print('Second is faster')