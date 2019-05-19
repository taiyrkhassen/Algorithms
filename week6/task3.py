def hiking(w,arr1,arr2):
    colorie=0
    n=len(arr1)
    arr3=[]  
    arr4=[]
    for i in range(n):
        arr4.append(0)
        
    d={}
    
    for i in range(n):
        count=int(arr2[i]/arr1[i])
        arr3.append(count)

    for i in range(n):
        d[arr3[i]] = arr1[i]
        
    arr3.sort()
    arr3.reverse()

    for i in arr3:
        if w==0:
            break
        if w-d[i]>0:
            w-=d[i]
            colorie+=d[i]*i
            index=arr1.index(d[i])
            arr4[index] = d[i]
        else:
            colorie+=i*w
            index=arr1.index(d[i])
            arr4[index]=w
            w=0
            
    print(colorie)
    print(arr4)
   
        

w=3
arr1=[4,2,5]
arr2=[2000,3000,1500]
hiking(w,arr1,arr2)
