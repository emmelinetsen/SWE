import unittest


def magic_index(arr):
    # for i, e in enumerate(arr):
    #     if i == e:
    #         return True
    # return False

    start, end = 0, len(arr) - 1
    # while start <= end:
    #     mid = int((start + end) / 2)
    #     if mid == arr[mid]:
    #         return True
    #     elif mid < arr[mid]:
    #         # check left side
    #         end = mid - 1
    #     elif mid > arr[mid]:
    #         start = mid + 1
    # return False
    return magic_idx(arr, start, end)

def magic_idx(arr, start, end):
    while start <= end:
        mid = int((start + end) / 2)
        if mid == arr[mid]:
            return True
        elif mid < arr[mid]:
            # check left side
            return magic_idx(arr, start, mid - 1)
        elif mid > arr[mid]:
            return magic_idx(arr, mid + 1, end)
    return False

class Test(unittest.TestCase):
    def test_magic_index_false(self):
        a = [1,2,3]
        self.assertEqual(False, magic_index(a))

    def test_magic_index_true(self):
        a = [-1,0,2]
        self.assertEqual(True, magic_index(a))

    def test_magic_index_not_unique(self):
        a = [-1,-1,-1,3,4]
        self.assertEqual(True, magic_index(a))

if __name__ == "__main__":
    Test.main()
