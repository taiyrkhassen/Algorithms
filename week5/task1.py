def sort(A):
    n = 0
    for i in range(len(A)):
        m = i
        for j in range( i + 1, len(A)):
            n+=1
            if A[m] > A[j]:
                m = j
        A[i], A[m] = A[m], A[i]
    
l = [17,3,33,42,29,15,119,23]
sort(l)
print(l)
