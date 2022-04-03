import unittest
# Remove duplicates from an unsorted linked list

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    head = None
    tail = None

    def __init__(self, arr):
        self.head = self.tail = Node() # sentinel node
        for i in arr:
            self.append(i)

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def return_array(self):
        ptr = self.head.next
        arr = []
        while ptr is not None:
            arr.append(ptr.value)
            # print(ptr.value, end=", ")
            ptr = ptr.next
        return arr

    def removeDups(self):
        s = set()
        ptr, prev = self.head.next, self.head
        while ptr is not None: # O(n), n= length of linked list
            if ptr.value not in s:
                s.add(ptr.value)
                ptr = ptr.next
                prev = prev.next
            else:
                prev.next = ptr.next
                ptr = ptr.next

    # removing duplicates without temporary buffer
    def removeDups2(self):
        # start from first node, iterate through rest to compare for dups. if dup, remove
        # continue to next node until the end

        # start = prev = self.head
        # end = start.next
        #
        # while start is not None and end is not None:
        #     while end is not None and prev is not None:
        #         if start.value == end.value:
        #             # remove dup
        #             prev.next = end.next
        #             end = end.next
        #         else:
        #             # continue
        #             prev = prev.next
        #             end = end.next
        #     start = prev = start.next
        #     if start is not None:
        #         end = start.next

        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


class TestLinkedList1(unittest.TestCase):
    def test_oneDup(self):
        ll = LinkedList([3,4,5,6,4])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_noDup(self):
        ll = LinkedList([3,4,5,6])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_noNodes(self):
        ll = LinkedList([])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [])

    def test_oneNode(self):
        ll = LinkedList([1])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [1])

    def test_twoNodes(self):
        ll = LinkedList([2,2])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [2])

    def test_mulitpleSameDups(self):
        ll = LinkedList([3,4,5,6,4,4,4,4])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_firstAndLastDup(self):
        ll = LinkedList([5,4,3,6,4,3,5])
        ll.removeDups()
        self.assertEqual(ll.return_array(), [5,4,3,6])

class TestLinkedList2(unittest.TestCase):
    def test_oneDup(self):
        ll = LinkedList([3,4,5,6,4])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_noDup(self):
        ll = LinkedList([3,4,5,6])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_noNodes(self):
        ll = LinkedList([])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [])

    def test_oneNode(self):
        ll = LinkedList([1])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [1])

    def test_twoNodes(self):
        ll = LinkedList([2,2])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [2])

    def test_mulitpleSameDups(self):
        ll = LinkedList([3,4,5,6,4,4,4,4])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [3,4,5,6])

    def test_firstAndLastDup(self):
        ll = LinkedList([5,4,3,6,4,3,5])
        ll.removeDups2()
        self.assertEqual(ll.return_array(), [5,4,3,6])
if __name__ == "__main__":
    unittest.main()