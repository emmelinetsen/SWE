def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        print("next_even ", next_even,"next_odd ", next_odd)
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            print("A[next_even] ", A[next_even],
                  "A[next_odd] ", A[next_odd], "\n")
            # print("next_odd ", next_odd, "A[next_odd] ", A[next_odd], "\n")
            next_odd -= 1
    return A
if __name__ == "__main__":
    print(even_odd([1,2,3,4,5]))