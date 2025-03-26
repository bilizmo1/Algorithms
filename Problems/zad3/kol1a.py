from kol1atesty import runtests

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







def canonical_form(s):
    return min(s,s[::-1])


def g(T):
    for i in range(len(T)):
        T[i] = canonical_form(T[i])
    T = merge_sort(T)

    max_strong = 0
    i = 0
    while i < len(T):

        strong = 0
        j = i
        while i < len(T) and j < len(T) and T[i] == T[j]:
            strong += 1
            j += 1
        if strong > max_strong:
            max_strong = strong
        i = j

    return max_strong


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )