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

    def addCycle(self, position):
        p = self.head
        for i in range(position):
            p = p.next
        self.tail.next = p

    def returnNodeAtPosition(self, position):
        p = self.head
        for i in range(position):
            p = p.next
        return p

    def hasLoop(self):
        p1 = self.head
        if self.head.next:
            p2 = self.head.next.next
        else:
            return False

        while p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                return False
        return False

class TestLinkedList(unittest.TestCase):
    def test_hasLoop_false_multipleNodes(self):
        ll = LinkedList([1,2,3])
        self.assertEqual(ll.hasLoop(), False)

    def test_hasLoop_false_2Nodes(self):
        ll = LinkedList([1,2])
        self.assertEqual(ll.hasLoop(), False)

    def test_hasLoop_false_oneNode(self):
        ll = LinkedList([1])
        self.assertEqual(ll.hasLoop(), False)

    def test_hasLoop_true(self):
        ll = LinkedList([1,2,3,4,5])
        ll.addCycle(4)
        self.assertEqual(ll.hasLoop(), ll.returnNodeAtPosition(4))