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


T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

for i in range(len(T)):
    T[i] = canonical_form(T[i])


T = merge_sort(T)

max_strong = 0
i = 0
while i < len(T):

    strong = 0
    j = i + 1
    while i < len(T) and j < len(T) and T[i] == T[j]:
        print(T[i], T[j], i, j)
        strong += 1
        j += 1
    print("j ----", j)
    if strong > max_strong:
        max_strong = strong
    i = j


print(max_strong)

