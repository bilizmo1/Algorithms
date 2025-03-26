from kol1testy import runtests



def min_heapify(A,n,i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and A[left] < A[smallest]:
        smallest = left
    if right < n and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        min_heapify(A,n,smallest)
def build_heap(A):
    n = len(A)
    for i in range(n//2-1,-1,-1):
        min_heapify(A,n,i)
    return A
def ksum(T, k, p):
    n = len(T)
    suma = 0

    for i in range(n-p + 1):
        heap = build_heap(T[i:i+k])
        window = T[i:i+p]
        for j in range(k,p):
            if heap[0] < window[j]:
                heap[0] = window[j]
            min_heapify(heap,len(heap),0)
        suma += heap[0]

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )