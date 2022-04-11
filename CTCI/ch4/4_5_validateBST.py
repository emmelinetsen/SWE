# check is binary tree is a BST
import math
import unittest


class BinaryTree:
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None


def isBST(root):
    arr = []

    def inOrder(node):
        if node:
            inOrder(node.left)
            arr.append(node.node)
            inOrder(node.right)

    inOrder(root)
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def isBST_simplified(root):
    global lastNode
    lastNode = None
    def inOrder(node):
        global lastNode
        if not node:
            return True
        if not inOrder(node.left):
            return False
        if lastNode and lastNode >= node.node:
            return False
        lastNode = node.node
        if not inOrder(node.right):
            return False
        return True
    return inOrder(root)
    lastNode = None

class Test(unittest.TestCase):
    def test_isBST_True(self):
        a = BinaryTree(1)
        b = BinaryTree(2)
        c = BinaryTree(3)

        b.left = a
        b.right = c

        self.assertEqual(True, isBST_simplified(b))

    def test_isBST_True(self):
        a = BinaryTree(1)

        self.assertEqual(True, isBST_simplified(a))

    def test_isBST_False(self):
        a = BinaryTree(5)
        b = BinaryTree(10)
        c = BinaryTree(14)
        d = BinaryTree(7)

        b.left = a
        b.right = c

        c.left = d

        self.assertEqual(False, isBST_simplified(b))

    def test_isBST_False_subTreeisBST_notComparedToParent(self):
        a = BinaryTree(5)
        b = BinaryTree(10)
        c = BinaryTree(14)
        d = BinaryTree(15)

        b.left = a
        b.right = c

        a.right = d

        self.assertEqual(False, isBST_simplified(b))
