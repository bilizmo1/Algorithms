def partition(A, l,r):
    x = A[r]
    j = l - 1
    for i in range(l,r):
        if  A[i] <= x:
            A[j + 1], A[i] = A[i], A[j + 1]
            j += 1
            print(j)
    A[j+1], A[r] = A[r], A[j+1]
    print(A)
    return j + 1






def quick_sort(A,l,r):
    if l < r:
        p = partition(A,l,r)
        quick_sort(A,l,p-1)
        quick_sort(A,p+1,r)
    return A


A = [12,8,4,3,1,5,6]
print(partition(A,0,len(A)-1))

print(quick_sort(A,0,len(A)-1))