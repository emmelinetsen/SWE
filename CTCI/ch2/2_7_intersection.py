import unittest

class Node:
    def __init__(self, value=0, next=None):
        self.value=value
        self.next=next

class LinkedList:
    head = None
    def __init__(self, arr):
        self.head = Node()
        for i in arr:
            self.append(i)

    def append(self, val):
        ptr = self.head
        while ptr.next:
            # prev = ptr
            ptr = ptr.next
        ptr.next = Node(val)

    def appendNode(self, node):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node

    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end=",")
            ptr = ptr.next

    def has_intersection(self, l1, l2):
        p1 = l1.head
        p2 = l2.head
        while p1.next:
            p1 = p1.next
        while p2.next:
            p2 = p2.next
        return p1 == p2

    def list_length(self, l):
        p = l.next
        len = 0
        while p:
            len+=1
            p = p.next
        return len

    def move_n_nodes_forward(self, l, n):
        p = l
        for i in range(n):
            p = p.next
        return p

    def intersection(self, l1, l2):
        if self.has_intersection(l1, l2):
            # need to check the length of the ll, cut out the nodes that are longer so can compare the same length
            p1 = l1.head.next
            p2 = l2.head.next
            p1_len = self.list_length(p1)
            p2_len = self.list_length(p2)

            if p1_len != p2_len:
                diff = p1_len - p2_len
                # p2_len greater than p1, iterate p2_len forward diff nodes
                if diff < 0:
                    p2 = self.move_n_nodes_forward(p2, abs(diff))
                else:
                    p1 = self.move_n_nodes_forward(p1, diff)

            # iterate through both ll until the intersecting node
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        else:
            return False


class TestLinkedList(unittest.TestCase):
    def test_intersection(self):
        l1 = LinkedList([1,2])
        l2 = LinkedList([5,6,10,11,13])
        node = LinkedList([4,5,6,7])
        l1.appendNode(node.head.next)
        l2.appendNode(node.head.next)
        print("L1")
        l1.print()
        print("\nL2")
        l2.print()
        self.assertEqual(LinkedList([]).intersection(l1,l2), node.head.next)

    def test_intersection_sameLength(self):
        l1 = LinkedList([1,2])
        l2 = LinkedList([5,63])
        node = LinkedList([4,5,6,7])
        l1.appendNode(node.head.next)
        l2.appendNode(node.head.next)
        print("L1")
        l1.print()
        print("\nL2")
        l2.print()
        self.assertEqual(LinkedList([]).intersection(l1,l2), node.head.next)

    def test_intersection_emptyLL(self):
        l1 = LinkedList([])
        l2 = LinkedList([5,6,10])
        node = LinkedList([4,5,6,7])
        # l1.appendNode(node.head.next)
        l2.appendNode(node.head.next)
        print("L1")
        l1.print()
        print("\nL2")
        l2.print()
        self.assertEqual(LinkedList([]).intersection(l1,l2), False)

    def test_intersection_noValuesinLL(self):
        l1 = LinkedList([])
        l2 = LinkedList([])
        node = LinkedList([4,5,6,7])
        # l1.appendNode(node.head.next)
        # l2.appendNode(node.head.next)
        print("L1")
        l1.print()
        print("\nL2")
        l2.print()
        self.assertEqual(LinkedList([]).intersection(l1,l2), False)

    def test_intersection_sameValuesNoIntersect(self):
        l1 = LinkedList([1,2,3,4,5,6,7])
        l2 = LinkedList([2,4,5,6,7])
        print("L1")
        l1.print()
        print("\nL2")
        l2.print()
        self.assertEqual(LinkedList([]).intersection(l1,l2), False)

if __name__ == "__main__":
    ll = LinkedList([1,2,3])
    ll.print()