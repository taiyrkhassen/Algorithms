def Search(arr, low, high):
    mid = int(low + (high -low)/2)
    if(arr[mid-1] > arr[mid] and arr[mid+1]>arr[mid]):
        return max(arr[mid-1], arr[mid+1])
    elif(high>low):
        
        return Search(arr, (mid+1), high)
    else:
        return Search(arr, (mid-1), high)

a = [35, 42, 5, 15, 27, 29]
n=len(a)
print(Search(a,0,n-1))                   
