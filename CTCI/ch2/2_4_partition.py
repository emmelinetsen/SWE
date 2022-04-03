import unittest


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    head = None
    tail = None

    def __init__(self, arr):
        self.head = self.tail = Node()
        for i in arr:
            self.append(i)

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def return_list(self):
        l = []
        tmp = self.head.next
        while tmp is not None:
            l.append(tmp.value)
            tmp = tmp.next
        return l

    # another way is to store small and large values in 2 ll
    # once we reach the end of the ll, do smallLL.tail.next = largeLL.head
    # there will be 4 pointers to keep track of, which can be confusing.
    # another approach can be to put the large values in a ll, while doing the same logic for pt1
    # once we reach the end of the ll, put ptr1.next = largeLL.head
    def partition(self, part): #O(length of ll) runtime
        ptr1 = ptr2 = self.head.next
        arr = [] #O(1) space
        while ptr2 is not None: #O(length of ll)
            if ptr2.value >= part:
                arr.append(ptr2.value)
            else:
                ptr1.value = ptr2.value
                ptr1 = ptr1.next
            ptr2 = ptr2.next
        for i in arr: #O(length of ll)
            ptr1.value = i
            ptr1 = ptr1.next

class TestLinkedList(unittest.TestCase):
    def test_partition_firstValueLessThanPartition(self):
        ll = LinkedList([3,5,8,5,10,2,1])
        ll.partition(5)
        self.assertEqual(ll.return_list(), [3,2,1,5,8,5,10])

    def test_partition_firstValueGreaterThanPartition(self):
        ll = LinkedList([8,5,8,5,10,2,1])
        ll.partition(5)
        self.assertEqual(ll.return_list(), [2,1,8,5,8,5,10])

    def test_partition_firstValueEqualToPartition(self):
        ll = LinkedList([5,5,8,5,10,2,1])
        ll.partition(5)
        self.assertEqual(ll.return_list(), [2,1,5,5,8,5,10])

    def test_partition_allValuesLessThanPartition(self):
        ll = LinkedList([1,2,3,4,2])
        ll.partition(5)
        self.assertEqual(ll.return_list(), [1,2,3,4,2])

    def test_partition_allValuesGreaterThanEqualToPartition(self):
        ll = LinkedList([8,5,8,5,10,5,20])
        ll.partition(5)
        self.assertEqual(ll.return_list(), [8,5,8,5,10,5,20])


if __name__ == "__main__":
    unittest.main()