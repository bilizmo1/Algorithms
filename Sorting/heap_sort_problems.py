"""
Napisz funkcję, która przyjmuje listę liczb i liczbę  k , a następnie znajduje i zwraca
 k  największych elementów tej listy, wykorzystując kopiec.
"""



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
    for i in range(n//2 -1, -1, -1):
        min_heapify(A,n,i)
    return A


def finder(A,k):
    n = len(A)
    heap = A[:k]
    heap = build_heap(A[:k])
    for i in range(k,n):
        if A[i] > heap[0]:
            heap[0] = A[i]
            min_heapify(heap,k,0)
    return heap


A = [4, 10, 3, 5, 1, 12, 7, 2]
k = 2

print(finder(A,k))



"""
Zadanie 3)
Zastosowanie kopca do znajdowania k najmniejszych elementów
"""


def max_heapify(A,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if i != largest:
        A[i],A[largest] = A[largest], A[i]
        max_heapify(A,n,largest)


