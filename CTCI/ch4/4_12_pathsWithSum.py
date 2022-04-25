import unittest
from queue import Queue

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def paths_with_sum(self, root, value):

        # implement a sort of BFS to go down the entire path to count the sum
        def get_sum(root, value, sum_val, total_count):
            sum_val += root.val
            if sum_val == value:
                total_count += 1
            if not root.left and not root.right:
                return total_count

            if root.left:
                total_count = get_sum(root.left, value, sum_val, total_count)
            if root.right:
                total_count = get_sum(root.right, value, sum_val, total_count)
            return total_count

        sum = 0
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            sum += get_sum(node, value, 0, 0)

        return sum
        # return get_sum(root, value, 0, 0)


class Test(unittest.TestCase):
    def test_paths_with_sum_from_root(self):
        a = BinaryTree(1)
        b = BinaryTree(-1)
        c = BinaryTree(1)
        a.left = b
        a.right = c
        self.assertEqual(1, a.paths_with_sum(a, 2))

    def test_paths_with_sum_besides_root(self):
        a = BinaryTree(1)
        b = BinaryTree(-1)
        c = BinaryTree(1)
        a.left = b
        a.right = c
        self.assertEqual(2, a.paths_with_sum(a, 1))

    def test_paths_with_sum_besides_root_2(self):
        a = BinaryTree(-1)
        b = BinaryTree(3)
        c = BinaryTree(1)
        d = BinaryTree(2)
        e = BinaryTree(1)
        f = BinaryTree(3)
        g = BinaryTree(3)
        h = BinaryTree(-3)
        i = BinaryTree(3)
        a.left = b
        a.right = c

        c.left = d
        c.right = g

        d.left = e
        e.right = f

        g.right = h
        h.right = i
        self.assertEqual(10, a.paths_with_sum(a, 3))
