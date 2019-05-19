def adssds(arr):
    y=len(arr)
    T=[]
    L=arr.copy()
    L.sort()
    print(L)
    
    
    
    for i in range(n):
        x=0
        for j in range(i+1):
            x+=L[j]
        T.append(x)
    total=0
    
    print(T)
    for i in range(n):
        total+=T[i]
    total/=n
    print(total)

    
    
        
        


arr=[500,100,300,200]
adddssd(arr)
