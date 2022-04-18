# create algorithm to determine if T2 is subtree of T1
# T1 is much bigger than T2
from queue import Queue
import unittest

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def checkSubtree(T1, T2):
    q = Queue()
    q.put(T1)
    while not q.empty():
        node = q.get()
        if node.val == T2.val and compareTree(node, T2):
            return True

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return False

def compareTree(T1, T2):
    node1 = T1
    node2 = T2
    if not node1 and node2 or node1 and not node2:
        return False
    if not node1 and not node2:
        return True

    if not compareTree(T1.left, T2.left):
        return False
    if T1.val != T2.val:
        return False
    if not compareTree(T1.right, T2.right):
        return False
    return True

# in order traversal to compare whether the two trees are the same
def compareSubtree(T1, T2):
    q1 = Queue()
    q2 = Queue()
    q1.put(T1)
    q2.put(T2)
    while not q1.empty() and not q2.empty():
        node1 = q1.get()
        node2 = q2.get()
        if node1.val != node2.val:
            return False
        if node1.left:
            q1.put(node1.left)
        if node2.left:
            q2.put(node2.left)
        if node1.right:
            q1.put(node1.right)
        if node2.right:
            q2.put(node2.right)
    return True


class Test(unittest.TestCase):
    def test_sameTree(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)

        d = TreeNode(1)
        e = TreeNode(2)
        f = TreeNode(3)

        a.left = b
        a.right = c

        d.left = e
        d.right = f
        self.assertEqual(True, checkSubtree(a, d))

    def test_smallSubtree(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)
        g = TreeNode(4)

        d = TreeNode(1)
        e = TreeNode(2)
        f = TreeNode(3)

        a.left = b
        a.right = c
        g.left = a

        d.left = e
        d.right = f
        self.assertEqual(True, checkSubtree(g, d))

    def test_not_sameSubtree(self):
        a = TreeNode(1)
        b = TreeNode(3)
        c = TreeNode(3)
        g = TreeNode(4)

        d = TreeNode(1)
        e = TreeNode(2)
        f = TreeNode(3)

        a.left = b
        a.right = c
        g.left = a

        d.left = e
        d.right = f
        self.assertEqual(False, checkSubtree(g, d))

if __name__ == "__main__":
    unittest.main()