from kol1testy import runtests

#Podejście naiwne

def merge(A, L,R):
    n = len(L)
    m = len(R)
    i = j = k = 0
    while i < n and j < m:
        if L[i][0] < R[j][0]:
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

def finder_two(T):
    n = len(T)
    B = n*[0]
    for i in range(n):
        B[i] = (T[i],i)
    B = merge_sort(B)
    maxi = 0
    for i in range(n):
        x = 0
        if B[i][1] < i:
            x = min(B[i][1],i)
        if maxi < x:
            maxi = x
    return maxi

def finder_one(T):
    n = len(T)
    max_rank = 0
    for i in range(1,n):
        counter = 0
        for j in range(i):
            if T[j] < T[i]:
                counter += 1
        if counter > max_rank:
            max_rank = counter
    return max_rank


def maxrank(T):
    return finder_two(T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )