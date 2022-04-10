import unittest
from queue import Queue

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    head = None
    tail = None
    def __init__(self, arr):
        self.head = Node()
        self.tail = self.head
        for i in arr:
            self.append(i)

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def printBinaryTree(self):
        tmp = self.head.next
        while tmp is not None:
            print(tmp.val.val, end="-> ")
            tmp = tmp.next
        print()

    def returnBinaryTree(self):
        tmp = self.head.next
        res = []
        while tmp is not None:
            res.append(tmp.val.val)
            # print(tmp.val.val, end="-> ")
            tmp = tmp.next
        return res

def list_of_depths(root):
    q = Queue()
    q.put(root)
    res = []
    nextLevel = Queue()
    while not q.empty():
        l = LinkedList([])
        while not q.empty():
            node = q.get()
            l.append(node)

            if node.left is not None:
                nextLevel.put(node.left)
            if node.right is not None:
                nextLevel.put(node.right)

        res.append(l)
        tmp = nextLevel
        nextLevel = q
        q = tmp

    return res

def list_of_depths_no_queues(root):
    current_level = LinkedList([root]) # linked list containing nodes at current level
    next_level = LinkedList([]) # linked list of containing nodes at next level
    node = current_level.head.next # starting node at current level; ptr to node on a LL
    res = [current_level] # resulting array containing multiple linked lists
    while node is not None:
        if node.val.left is not None: # if the left value of the binary tree isn't null
            next_level.append(node.val.left)
        if node.val.right is not None: # if the right value of the binary tree isn't null
            next_level.append(node.val.right)

        node = node.next # go to the next linked list node
        if node is None:
            if next_level.head.next is not None:
                res.append(next_level)
                node = next_level.head.next # assigning next_level linked list to node
                next_level = LinkedList([])
    return res



def return_result(result):
    res = []
    for i in result:
        # i.printBinaryTree()
        res.append(i.returnBinaryTree())
    return res

def print_result(result):
    res = []
    for i in result:
        i.printBinaryTree()
        # res.append(i.returnBinaryTree())
    return res

def bfs(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        print(node.val, end = ", ")
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

class TestMethod(unittest.TestCase):
    def test_listOfDepths(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")
        e = BinaryTree("e")
        f = BinaryTree("f")
        g = BinaryTree("g")

        a.left = b
        a.right = c
        self.assertEqual([['a'], ['b', 'c']], return_result(list_of_depths(a)))

    def test_listOfDepths_multipleLevelsWithEmptyLeaves(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")
        e = BinaryTree("e")
        f = BinaryTree("f")
        g = BinaryTree("g")
        h = BinaryTree("h")

        a.left = b
        a.right = c

        b.left = d
        b.right = e

        c.left = f

        d.left = g

        g.left = h

        print_result(list_of_depths(a))
        self.assertEqual([['a'], ['b', 'c'],['d', 'e', 'f'],['g'],['h']], return_result(list_of_depths(a)))
        self.assertEqual([['a'], ['b', 'c'],['d', 'e', 'f'],['g'],['h']], return_result(list_of_depths_no_queues(a)))
