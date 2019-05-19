import math
#1
def gcd3(a,b):
    a1 = a%b
    return (a*b)/(b*a1)
#2
def numOfDiv(n):
    a = 0
    while(n>1):
        n=n/2
        a+=1
    return a
#3
