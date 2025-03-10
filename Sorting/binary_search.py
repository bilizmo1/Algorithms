#implementation of BinarySearch


def binary_search(A, x):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            l = mid + 1
        else :
            r = mid - 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 3))
p
