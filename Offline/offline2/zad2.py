from zad2testy import runtests

def count_inversions(A):
    n = len(A)
    number_of_inversion = 0
    for i in range(n):
        for j in range(i, n):
            if A[i] > A[j]:
                number_of_inversion += 1

    return number_of_inversion


# Odkomentuj by uruchomic duze testy
#runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
