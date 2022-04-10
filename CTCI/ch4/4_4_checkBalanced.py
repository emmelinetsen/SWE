# check if binary tree is balanced
# balanced tree - tree such that the heights of the 2 subtrees of any node never differ more than 1

# using BFS: use queue to store the nodes that haven't been visited yet
# have 2 queues - one that is the current queue (current level) and another that has the next level nodes
# have an int variable hasNullNodes to check whether any of the children nodes have null nodes. +1 if there is
# if hasNullNodes has been set for next level, set a separate bool variable nullCheckedForLevel to T
# nullCheckedForLevel will be set back to false at the end of the current level
# if hasNullNodes > 2, then return false because it means the subtree height difference is more than 2 (leaves also
# have null nodes)

import unittest


class BinaryTree:
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None


# time complexity: O(N) where N is the # of nodes in the tree
# space complexity: O(2^H) where H is the height of the tree

def check_balanced(root):
    if not root:
        return True
    return abs(maxHeight(root.left) - maxHeight(root.right)) <= 1 and check_balanced(root.left) and check_balanced(
        root.right)


def maxHeight(root):
    if not root:
        return 0
    return max(maxHeight(root.left), maxHeight(root.right)) + 1


class Test(unittest.TestCase):
    def test_maxHeight_1(self):
        a = BinaryTree("a")

        self.assertEqual(1, maxHeight(a))

    def test_maxHeight_2(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")

        a.left = b
        a.right = c

        self.assertEqual(2, maxHeight(a))

    def test_maxHeight_3(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")

        a.left = b
        a.right = c

        b.left = d

        self.assertEqual(3, maxHeight(a))

    def test_checkBalanced_leftRightNodesPopulated(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")

        a.left = b
        a.right = c
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_singleNode(self):
        a = BinaryTree("a")

        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_empty(self):
        self.assertEqual(True, check_balanced([]))

    def test_checkBalanced_onlyLeftNodePopulated(self):
        a = BinaryTree("a")
        b = BinaryTree("b")

        a.left = b
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_heightDifference1_left(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")

        a.left = b
        a.right = c

        b.left = d
        self.assertEqual(True, check_balanced(a))

    def test_checkBalanced_heightDifference1_right(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")

        a.left = b
        a.right = c

        c.left = d
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

    def test_checkBalanced_heightDifference(self):
        a = BinaryTree("a")
        b = BinaryTree("b")
        c = BinaryTree("c")
        d = BinaryTree("d")
        e = BinaryTree("e")

        a.left = b
        a.right = c

        c.left = d
        c.right = e
        self.assertEqual(True, check_balanced(a))
