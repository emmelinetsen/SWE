import random

class QuickSort:

    def quicksort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        pivot = random.randint(0, len(arr)-1)
        less, greater = [], [] # to get an array with values less or greater than the value at pivot
        for i in range(0, pivot):
            if arr[i] <= arr[pivot]:
                less.append(arr[i])
            else:
                greater.append(arr[i])
        for i in range(pivot+1, len(arr)):
            if arr[i] <= arr[pivot]:
                less.append(arr[i])
            else:
                greater.append(arr[i])

        sorted_less = self.quicksort(less)
        sorted_greater = self.quicksort(greater)
        sorted_arr = []
        for i in sorted_less:
            sorted_arr.append(i)
        sorted_arr.append(arr[pivot])
        for i in sorted_greater:
            sorted_arr.append(i)
        return sorted_arr

if __name__ == "__main__":
    arr = QuickSort()
    print(arr.quicksort([7,1,4,6,3,5]))