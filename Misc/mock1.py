# given an array of integers, count the # of occurrences of each integer
# [1,1,2,3] -> {1:2, 2:1, 3:1}

# iterate through the arr, instaniate result dict that contains the # of occurence for each int
# if the int is not in the dict
## add that int into the dictionary, and set the count to 1
# if the int is in the dict
## +1 to the current count for that int


# if given a sorted array, how does this change the algorithm?
# [1,1,2,2,2,3] -> {1:2, 2:3, 3:1}
# [1,1,2,2,3,4,5,6,6,7]

# to find the start/end of a number:
# start of num at arr[i]: the arr[i-1] number would be diff than arr[i]
# end of num at arr[i]: the arr[i+1] number would be diff than arr[i]

# split the arr in half -> arr[0:len(arr)/2] and arr[len(arr)/2+1:len(arr)-1]

# binary search: input - number, output - position
# if there are multiple of the same #, the bs would return the first occurence of that # when it's searching
# if there are no occur. of that #, you would know the position for where that # should be

# searching for the first

# O(mlogn) where n is the len of arr, m is the largest occurrence of an int
# start at the first #
# do a binary search of that #



def num_occurrences(arr):
    res = dict()
    for i in arr:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res

