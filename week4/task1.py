import timeit
#1-t
def an(n):
    if n==1 or n==2 or n==3:
        return 1
    else:
        return an(n-1) + an(n-2) + an(n-3)
#2-t    
def ar(n):
    L = [1,1,1]
    for i in range(2,n):
        L.append(L[i-2] + L[i-1] + L[i])
    return L[n]

#4-t
a = int(input("Enter a number: "))
start = timeit.default_timer()
print(an(a))
stop = timeit.default_timer()
print('Time: ', stop - start)
