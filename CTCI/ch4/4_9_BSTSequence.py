import unittest
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def BST(root):
    res = [root]
    print_permutations(res)

def print_permutations(l):
    # find possible next values from the list
    next_values = possible_values(l)
    if len(next_values) == 0:
        print_sequence(l)
        print()
    else:
        for value in next_values:
            l.append(value)
            print_permutations(l)
            l.remove(value)


def possible_values(l):
    res = []
    for node in l:
        if node.left and node.left not in l:
            res.append(node.left)
        if node.right and node.right not in l:
            res.append(node.right)
    return res

def print_sequence(sequence):
    for i in sequence:
        print(i.val, end=", ")

class Test(unittest.TestCase):


    def test_BST_sequence(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)

        b.left = a
        b.right = c
        BST(b)

    def test_BST_sequence_2(self):
        a = Node(8)
        b = Node(4)
        c = Node(10)
        d = Node(2)

        a.left = b
        a.right = c
        b.left = d
        BST(a)