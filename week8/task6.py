p = [50000, 20000, 40000]
d = [5,3,1]
maxd = max(p)

w = list(zip(p,d))
sp = sorted(w, reverse=True)
print(sp)
slot = []
for i in range( 0, len(p)):
    slot[i] = -1
for i in range(0, len(p)):
    k = min(maxd, d[i])
    while k>=1:
        if(slot[k] == -1):
            slot[k] = p[i]
            break
        k = k-1
print(slot)
