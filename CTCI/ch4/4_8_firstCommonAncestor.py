# find first common ancestor of two nodes in a binary tree
# find the height of both nodes
# if height of both nodes are not the same, traverse nodes so they are at the same height
# compare whether nodes are equal each other. if not, move both up by 1 height until they're equal
import unittest

class Node:
    def __init__(self, node, parent):
        self.node = node
        self.left = None
        self.right = None
        self.parent = parent

def firstCommonAncestor(node1, node2):
    node1_h = height(node1)
    node2_h = height(node2)
    if node1_h != node2_h:
        diff = node1_h - node2_h
        if diff > 0: # node 1 has larger height
            traverse_levels_up(node1, diff)
        else:
            traverse_levels_up(node2, abs(diff))
    while node1 and node2 and node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1



def height(node):
    h = 1
    while node.parent:
        h += 1
        node = node.parent
    return h

def traverse_levels_up(node, levels):
    for i in range(levels):
        if node:
            node = node.parent
        else:
            raise IndexError("Cannot traverse higher.")

class Test(unittest.TestCase):
    def test_firstCommonAncestor(self):
        a = Node(1, None)
        b = Node(2, a)
        c = Node(3, a)

        a.left = b
        a.right = c
        self.assertEqual(a, firstCommonAncestor(b, c))
