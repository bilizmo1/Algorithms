"""
Napisz funkcję quick_select(), która znajduje k-ty najmniejszy element w nieposortowanej tablicy,
używając algorytmu QuickSelect
"""





def partition(A,l,r):
    x = A[r]
    j = l - 1
    for i in range(l,r):
        if A[i] <= x:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[j+1],A[r] = A[r],A[j+1]
    print(A)
    return j+1


def quick_select(A,k):
    n = len(A)
    l = 0
    r = n - 1
    k -= 1 # interesuje nas indeks 
    while l <= r:
        p = partition(A,l,r)
        print(p,l,r)
        if p == k:
            print(A[k])
            return A[k]
        elif p > k:
            r = p - 1
        else:
            l = p + 1


A = [12,4,1,5,3,8,9,10]
quick_select(A,3)
