V=float(input("Enter your money in dollars:"))
V=int(V*100) 
C=[10,25,50]

x=len(C)-1
while V!=0:
    count=V//C[x]
    V=V%C[x]
    if count!=0:
        print(str(count)+' X '+str(C[x])+' cents')
    x-=1

    
    
    

