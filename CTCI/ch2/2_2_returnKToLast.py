import unittest


# Find kth to last element in a singly linked list
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

    def returnKToLast(self, k):
        current = runner = self.head
        if k == 0:
            return self.tail.value

        for i in range(k):  # move runner node k steps ahead
            if runner is None:  # out of bounds
                return 0
            runner = runner.next
        while runner is not None:
            current = current.next
            runner = runner.next
        return current.value


class TestLinkedList(unittest.TestCase):
    def test_kToLast(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(ll.returnKToLast(2), 4)

    def test_kOutOfBounds(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(ll.returnKToLast(6), 0)

    def test_kSameLength(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(ll.returnKToLast(5), 1)

    def test_kIsZero(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(ll.returnKToLast(0), 5)

    def test_emptyLL(self):
        ll = LinkedList([])
        self.assertEqual(ll.returnKToLast(2), 0)


if __name__ == "__main__":
    unittest.main()
