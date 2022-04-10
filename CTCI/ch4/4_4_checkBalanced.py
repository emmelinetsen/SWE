# check if binary tree is balanced
# balanced tree - tree such that the heights of the 2 subtrees of any node never differ more than 1

# using BFS: use queue to store the nodes that haven't been visited yet
# have 2 queues - one that is the current queue (current level) and another that has the next level nodes
# have an int variable hasNullNodes to check whether any of the children nodes have null nodes. +1 if there is
# if hasNullNodes has been set for next level, set a separate bool variable nullCheckedForLevel to T
# nullCheckedForLevel will be set back to false at the end of the current level
# if hasNullNodes > 1, then return false because it means the subtree height difference is more than 1

from queue import Queue
import unittest

class BinaryTree:
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None

def check_balanced(root):
    currentLevel = Queue()
    nextLevel = Queue()
    currentLevel.put(root)
    hasNullNodes = 0
    nullCheckedForLevel = False

    while not currentLevel.empty():
        if hasNullNodes > 1:
            return False
        node = currentLevel.get()
        if node.left is not None:
            nextLevel.put(node.left)
        if node.left is None and not nullCheckedForLevel: # not counting for null nodes of the same level
            hasNullNodes += 1
            nullCheckedForLevel = True
        if node.right is not None:
            nextLevel.put(node.right)
        if node.right is None and not nullCheckedForLevel: # not counting for null nodes of the same level
            hasNullNodes += 1
            nullCheckedForLevel = True

        if currentLevel.empty(): # finished iterating through the current level
            tmp = currentLevel
            currentLevel = nextLevel
            nextLevel = tmp
            nullCheckedForLevel = False
    return True

class Test(unittest.TestCase):
    def test_checkBalanced_leftRightNodesPopulated(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")

        a.left = b
        a.right = c
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_onlyLeftNodePopulated(self):
        a = BinaryTree("a")
        b = BinaryTree("b")

        a.left = b
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_heightDifference1(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")

        a.left = b
        a.right = c

        b.left = d
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_heightDifference2(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")
        e = BinaryTree("e")

        a.left = b
        a.right = c

        b.left = d

        d.left = e
        self.assertEqual(False, check_balanced(a))
