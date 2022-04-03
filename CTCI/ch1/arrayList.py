# copy copies a into b. E.g
# a = [1,2], b=[,,,,,,]
# b = [1,2,,,,,]
def copy(a, b): #O(a)
    for i in range(len(a)):
        b[i] = a[i]
    return b

class ArrayList:
    arr = [None] * 2
    curr_list_len = 0

    def get(self, i): # O(1)
        if i < 0 or i >= self.curr_list_len:
            print("Error")
            return False
        return self.arr[i]

    def set(self, i, value): # O(1)
        if i < 0 or i >= self.curr_list_len:
            return False
        self.arr[i] = value

    def append(self, x):
        if self.curr_list_len < len(self.arr): # O(1)
            self.arr[self.curr_list_len] = x
            self.curr_list_len += 1
        else: #O(current length)
            # newArr = [None] * (len(self.arr) * 2) # O(1)
            newArr = [None] * (len(self.arr) + 3) # O(1)
            self.arr = copy(self.arr, newArr) # O(current length)
            self.arr[self.curr_list_len] = x
            self.curr_list_len += 1