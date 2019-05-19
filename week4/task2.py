import timeit
def Max_gcd(a,b):
    best = 0
    for d in range(1,a + b):
        if (a%d)==0 and (b%d)==0:
            best=d
    return best


def Aid_gcd(a,b):
    if b==0:
        return a
    else:
        a1 = a%b
        return Aid_gcd(b,a1)

start1 = timeit.default_timer()
Max_gcd(1245781223, 3265983217)
stop1 = timeit.default_timer()

print('Time of Max\'s Brute-force algorithm: ', stop1 - start1) 


start2 = timeit.default_timer()
Aid_gcd(1245781258, 3274659832)
stop2 = timeit.default_timer()

print('Time of Aigerim\'s Euclid’s algorithm: ', stop2 - start2)

