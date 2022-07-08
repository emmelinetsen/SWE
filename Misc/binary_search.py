import unittest
# given a sorted array, perform binary search using recursion
# finding either the left most or right most
# [1,1,2,2,2,3] -> bs(2) = result would either be 2 or 4
# should also return where the number would be if the number doesn't exsit in the array


# input: array of integers, number to search
# output:
## if exist: the position of the left most number
## doesn't exist: the position where the number would be

def bs(arr, num):
    start = 0
    end = len(arr)-1
    mid = (end-start)//2
    if arr[mid] == num:
        return mid
    if arr[mid] < num:
        return 1 + bs(arr[mid+1], num)
    else:
        return bs(arr[0:mid], num)
    # didn't find the number
    if len(arr) == 1:
        return

def binary_search(arr, num):
    start = 0
    end = len(arr)-1
    mid = (end - start)//2

    # accounting for values not in the array
    if len(arr) == 1 and arr[mid] != num:
        return 1 if arr[mid] < num else 0

    if arr[mid] == num:
        if mid != 0 and arr[mid-1] != num or mid == 0: # left value
            return mid
        else: # search the left side of the array for the value
            return binary_search(arr[0:mid], num)
    else:
        if arr[mid] < num: # if the number is smaller than mid, binary search the right side
            return mid + 1 + binary_search(arr[mid+1:], num)
        else: # otherwise do binary search on the left side of the array
            return binary_search(arr[0:mid], num)


if __name__ == "__main__":
    arr = [1,1,2,2,2,2,2,3,3,4]
    print(binary_search(arr,2.5))

    arr_2 = [1,2,3,4]
    print(bs(arr_2,2))


