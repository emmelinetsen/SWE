class MergeSort:
    def __init__(self, numbers):
        self.values = numbers
        self.count = len(numbers)

    def sort(self):
        self.merge_sort(0, self.count -1)

    # low = the left side of the array (self). the lowest position in the array
    # high = the right side of the array (self). the highest position in the array
    # merge_sorts sorts the subarray from low to high. So all the elements in low to high
    ## will be sorted.
    def merge_sort(self, low, high):
        if low == high:
            return
        else:
            mid = (low + high)//2
            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            self.merge(low, mid, high)

    # merge two arrays together
    # low = the lowest position in the array
    # mid = the middle position in the array. mid + 1 will denote the position to start for the second array to merge
    # high = the highest position/upper bound of the array to merge
    def merge(self, low, mid, high):
        tmp = [] # creating a temporary array to store the sorted array
        p1 = low
        p2 = mid+1
        while p1 <= mid and p2 <= high:
            if self.values[p1] <= self.values[p2]:
                tmp.append(self.values[p1])
                p1 += 1
            else:
                tmp.append(self.values[p2])
                p2 += 1

        while p1 <= mid:
            tmp.append(self.values[p1])
            p1 += 1

        while p2 <= high:
            tmp.append(self.values[p2])
            p2 += 1

        tmp_ptr = 0
        # update the array from low to high with the values in tmp
        for i in range(low, high+1):
            self.values[i] = tmp[tmp_ptr]
            tmp_ptr += 1


if __name__ == "__main__":
    arr = MergeSort([5,3,1,2,7,6])
    arr.sort()
    print(arr.values)