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

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def append_to_head(self, val):
        if self.head == self.tail:
            self.tail.value = val
            self.head = Node()
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head.value = val
            self.head = Node()
            self.head.next = tmp

    def return_list(self, ll):
        ptr = ll
        res = []
        while ptr is not None:
            res.append(ptr.value)
            ptr = ptr.next
        return res

    def sumLists(self, l1, l2):
        sum = self.getNumericValueFromLinkedList(l1) + self.getNumericValueFromLinkedList(l2)

        # both values in ll are 0
        if sum == 0:
            return self.head

        res = LinkedList([])
        while sum != 0:
            res.append(sum % 10)
            sum = int(sum / 10)
        return res.head.next

    def sumListsReversed(self, l1, l2):
        sum = self.getNumericValueFromLinkedListReversed(l1) + self.getNumericValueFromLinkedListReversed(l2)

        if sum == 0:
            return self.head

        res = LinkedList([])
        while sum != 0:
            res.append_to_head(sum % 10)
            sum = int(sum/10)
        return res.head.next

    def getNumericValueFromLinkedList(self, ll):
        num = 0
        ptr = ll.head.next
        i = 0
        while ptr is not None:
            num += int(ptr.value * 10 ** (i))
            i += 1
            ptr = ptr.next
        return num

    def linkedListLength(self, ll):
        ptr = ll.head.next
        len = 0
        while ptr is not None:
            len += 1
            ptr = ptr.next
        return len

    def getNumericValueFromLinkedListReversed(self, ll):
        len = self.linkedListLength(ll)
        ptr = ll.head.next
        num = 0

        while ptr is not None and len > 0:
            num += int(ptr.value * (10 ** (len - 1)))
            ptr = ptr.next
            len -= 1
        return num


class TestLinkedList(unittest.TestCase):
    def test_sumLists(self):
        l = LinkedList([])
        sum = l.sumLists(LinkedList([7, 1, 6]), LinkedList([5, 9, 2]))
        self.assertEqual(l.return_list(sum), [2, 1, 9])

    def test_sumListsDifferentLengths(self):
        l = LinkedList([])
        sum = l.sumLists(LinkedList([76]), LinkedList([5, 9, 2]))
        self.assertEqual(l.return_list(sum), [1, 7, 3])

    def test_sumListsOneEmptyLL(self):
        l = LinkedList([])
        sum = l.sumLists(LinkedList([]), LinkedList([5, 9, 2]))
        self.assertEqual(l.return_list(sum), [5, 9, 2])

    def test_sumListsBothEmptyLL(self):
        l = LinkedList([])
        sum = l.sumLists(LinkedList([]), LinkedList([]))
        self.assertEqual(l.return_list(sum), [0])

    def test_sumListsReversed(self):
        l = LinkedList([])
        sum = l.sumListsReversed(LinkedList([6, 1, 7 ]), LinkedList([2, 9, 5]))
        self.assertEqual(l.return_list(sum), [9, 1, 2])

    def test_sumListsReversedDifferentLengths(self):
        l = LinkedList([])
        sum = l.sumListsReversed(LinkedList([61 ]), LinkedList([2, 9, 5]))
        self.assertEqual(l.return_list(sum), [3,5,6])

    def test_sumListsReversedOneEmpty(self):
        l = LinkedList([])
        sum = l.sumListsReversed(LinkedList([]), LinkedList([2, 9, 5]))
        self.assertEqual(l.return_list(sum), [2, 9, 5])

    def test_sumListsReversedBothEmpty(self):
        l = LinkedList([])
        sum = l.sumListsReversed(LinkedList([]), LinkedList([]))
        self.assertEqual(l.return_list(sum), [0])

if __name__ == "__main__":
    unittest.main()
