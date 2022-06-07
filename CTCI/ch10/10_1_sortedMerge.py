# given 2 sorted arrays A and B where A has a large enough buffer at the end to hold B
# merge B into A in sorted order

# brute force - create a new array c. this array would hold both sorted values in a and b
# have a pointer at the beginning of both array a and b
# compare whether a.ptr or b.ptr is smaller, place the smaller value in c
# return c

def sorted_merge(a, b):
    # start with the back of array a
    # have a ptr a for the position of the last value in a. to achieve this, iterate from the back until the position
    # has a value
    # have a ptr b for the position of the last value in b
    # compare which value in a.ptr and b.ptr is larger, place that value in the back of array a
    # continue until iterate through both a and b

    ptr = len(a) - 1
    ptr_a, ptr_b = ptr, len(b) - 1

    while a[ptr_a] is None: # ptr_a will keep decrementing until a value at pos ptr_a is not None
        ptr_a -= 1

    while ptr_a >= 0 and ptr_b >= 0:
        if a[ptr_a] >= b[ptr_b]:
            a[ptr] = a[ptr_a]
            ptr_a -= 1
        else:
            a[ptr] = b[ptr_b]
            ptr_b -= 1
        ptr -= 1

    # one of the arrays reached 0, adding remaining values into a
    while ptr_a >= 0:
        a[ptr] = a[ptr_a]
        ptr_a -= 1
        ptr -= 1

    while ptr_b >= 0:
        a[ptr] = b[ptr_b]
        ptr_b -= 1
        ptr -= 1

    return a

if __name__ == "__main__":
    a = [1,12,34,45,None,None,None]
    b = [3,4,8]
    print(sorted_merge(a, b))