def merge(A, L,R):
    n = len(L)
    m = len(R)
    i = j = k = 0
    while i < n and j < m:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n:
        A[k] = L[i]
        i += 1
        k += 1
    while j < m:
        A[k] = R[j]
        j += 1
        k += 1
    return A




def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    A = merge(A, L,R)
    return A



A = [12,3,1,4,6,12,3,4,5,6,0]


print(merge_sort(A))


