# find next node (in order successor) of a given node in a bst
import unittest

class BinaryTree:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

def successor(tree, node):
    arr = []
    def inOrder(root):
        if root:
            inOrder(root.left)
            arr.append(root)
            inOrder(root.right)

    inOrder(tree)
    for i in range(len(arr)):
        if arr[i] == node and i != len(arr) - 1:
            return arr[i+1]
    return None

def successor(node):
    if node.right:
        # if there is a right node, get the left most node
        return get_leftmost_node(node)
    else:
        # need to go to the top most parent level and return the parent
        # keep going up until node == parent.left
        while node.parent and node.parent.left != node:
            node = node.parent
        return node.parent

def get_leftmost_node(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

class Test(unittest.TestCase):
    def test_successor(self):

        b = BinaryTree(2,None)
        a = BinaryTree(1,b)
        c = BinaryTree(3,b)

        b.left = a
        b.right = c
        self.assertEqual(b, successor(a))

    def test_successor_rootNode(self):

        b = BinaryTree(2,None)

        self.assertEqual(None, successor(b))