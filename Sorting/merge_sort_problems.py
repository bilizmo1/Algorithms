"""
Zadanie 1) Sortowanie krotek
Napisz funkcję, która będzie sortować listę krotek. Każda krotka ma dwa elementy,
z których drugi (indeks 1) jest kluczem sortującym

A = [(1, 5), (3, 2), (4, 6), (2, 1)]
result

"""

def merge(A,L,R):
    n = len(L)
    m = len(R)
    i = j = k = 0
    while i < n and j < m:
        if L[i][1] < R[j][1]:
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
    mid = len(A)//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    A = merge(A,L,R)
    return A


A = [(1, 5), (3, 2), (4, 6), (2, 1)]

print(merge_sort(A))

"""
Zadanie 2)
Liczba inwersji => Odwrotności to sytuacje, kiedy para elementów w liście 
jest odwrotnie uporządkowana, czyli A[i] > A[j] i i < j
"""


def count_inverions(A,L,R):
    n = len(L)
    m = len(R)
    i = j = k = 0
    inversion = 0
    while i < n and j < m:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            inversion += n - i
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
    return A, inversion


def counter(A,inverion):
    if len(A) <= 1:
        return A,inverion
    mid = len(A)//2
    L, inverion= counter(A[:mid],inverion)
    R ,inverion = counter(A[mid:],inverion)
    A,res = count_inverions(A,L,R)[0],count_inverions(A,L,R)[1]
    inverion += res
    return A,inverion

B = [2, 3, 8, 6, 1]

print(counter(B,0))