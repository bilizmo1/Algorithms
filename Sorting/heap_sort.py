def heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[left] > A[largest]:
        largest = left

    if right < n and A[right] > A[largest]:
        largest = right
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def build_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n - 1, -1, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    print(A)


heap_sort([5, 4, 3, 2, 1])

# kopiec min



def heapify_min(A,n,i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[left] < A[ smallest]:
        smallest = left
    if right < n and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        heapify_min(A,n,smallest)

def build_min_heap(A):
    n = len(A)
    for i in range(n//2 -1, -1, -1):
        heapify_min(A,n,i)

def min_heap_sort(A):
    n = len(A)
    build_min_heap(A)
    for i in range(n-1,-1,-1):
        A[i], A[0] = A[0], A[i]
        heapify_min(A,i,0)
    print(A)

min_heap_sort([1,32,12,4,2,5,1])