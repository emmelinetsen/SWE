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

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=",")
            tmp = tmp.next

    def return_list(self):
        l = []
        tmp = self.head.next
        while tmp is not None:
            l.append(tmp.value)
            tmp = tmp.next
        return l

    def get_i_node(self, i):
        tmp = self.head.next
        for j in range(i):
            tmp = tmp.next
        return tmp

    # don't have reference to previous node, need to update the value of current node
    # and assign node.next to node.next.next to avoid duplicate nodes with the same values
    def delete_middle_node(self, node):
        if node.next is not None:
            node.value = node.next.value
            node.next = node.next.next
        else:
            raise IndexError("Can't delete last node without additional reference to list.")

class TestLinkedList(unittest.TestCase):
    def test_getINode(self):
        ll = LinkedList([1,4,8,19])
        node = ll.get_i_node(2)
        self.assertEqual(node.value, 8)

    def test_deleteMidNode(self):
        ll = LinkedList([1,4,8,19])
        node = ll.get_i_node(2)
        ll.delete_middle_node(node)
        self.assertEqual(ll.return_list(), [1,4,19])

    def test_3Nodes(self):
        ll = LinkedList([1,4,8])
        node = ll.get_i_node(1)
        ll.delete_middle_node(node)
        self.assertEqual(ll.return_list(), [1,8])

    def test_deleteSecondToLastNode(self):
        ll = LinkedList([1,4,8,9,12,15])
        node = ll.get_i_node(4)
        ll.delete_middle_node(node)
        self.assertEqual(ll.return_list(), [1,4,8,9,15])

    def test_deleteFirstNode(self):
        ll = LinkedList([1,4,8,9,12,15])
        node = ll.get_i_node(0)
        ll.delete_middle_node(node)
        self.assertEqual(ll.return_list(), [4,8,9,12,15])

    def test_deleteLastNode(self):
        ll = LinkedList([1,4,8,9,12,15])
        node = ll.get_i_node(5)
        with self.assertRaises(IndexError):
            ll.delete_middle_node(node)

if __name__ == "__main__":
    unittest.main()