def Peak(arr, low, high,n):

    mid = int(low + (high -low)/2)
    
    # Compare middle element with its  
    # neighbours (if neighbours exist) 
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return Peak(arr, low, (mid - 1), n)
 
    else: 
        return Peak(arr, (mid + 1), high, n) 


    
a = [10, 20, 15, 2, 23,90,67]
n = len(a)
print(Peak(a, 0, n-1, n))
