import unittest


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        # self.visited = False

    def set_children(self, arr):
        for i in arr:
            self.children.append(i)


def route_between_nodes(node1, node2, visited):
    if node1 == node2:
        return True
    elif node1 in visited:
        return False
    visited.add(node1)
    for neighbor in node1.children:
        if route_between_nodes(neighbor, node2, visited):
            return True
    return False

def route_between_nodes_iterative(node1, node2):
    # add all children of current node into stack
    # create stack to keep track of all the nodes that still need to be checked
    # pop the top of the stack to check whether node == node2. if yes, return true
    # if not, then pop off next node to determine whether it is equal to node2
    # at the end, if there hasn't been a node that == node2, return False

    visited = set()
    children = [node1]
    while len(children) != 0:
        n = children.pop()
        if n == node2:
            return True
        if n not in visited:
            visited.add(n)
            for i in n.children:
                children.append(i)
        # visited.add(n)
        # for i in n.children:
        #     if i not in visited:
        #         children.append(i)
    return False

class TestNode(unittest.TestCase):
    def test_route_between_nodes(self):
        a = Node("a")
        b = Node("b")
        b.set_children([a])
        g = Graph([a, b])
        self.assertEqual(route_between_nodes(b, a, set()), True)

    def test_route_between_nodes_loop(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        b.set_children([a])
        a.set_children([b])
        g = Graph([a, b])
        self.assertEqual(route_between_nodes(b, c, set()), False)
        self.assertEqual(route_between_nodes(a, b, set()), True)

    def test_route_between_nodes_iterative(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        b.set_children([c])
        a.set_children([b])
        # self.assertEqual(route_between_nodes_iterative(b, a), False)
        self.assertEqual(route_between_nodes_iterative(a, c), True)

    def test_route_between_nodes_iterative_circular(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        b.set_children([a])
        a.set_children([b])
        # self.assertEqual(route_between_nodes_iterative(b, a), True)
        self.assertEqual(route_between_nodes_iterative(a, c), False)

    def test_route_between_nodes_iterative_circular_2(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        b.set_children([a,c])
        a.set_children([b])
        self.assertEqual(route_between_nodes_iterative(b, a), True)
        self.assertEqual(route_between_nodes_iterative(a, c), True)

    def test_route_between_nodes_iterative_circular_3(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        b.set_children([a,c])
        a.set_children([b])
        c.set_children([d])
        self.assertEqual(route_between_nodes_iterative(b, d), True)
        self.assertEqual(route_between_nodes_iterative(a, d), True)
        self.assertEqual(route_between_nodes_iterative(a, a), True)
        self.assertEqual(route_between_nodes_iterative(a, b), True)

    def test_route_between_nodes_iterative_circular_4(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        a.set_children([b])
        b.set_children([c,d])
        c.set_children([d])
        d.set_children([a])
        self.assertEqual(route_between_nodes(a,c, set()), True)
        self.assertEqual(route_between_nodes_iterative(a, c), True)

    def test_route_between_nodes_iterative_circular_5(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.set_children([b])
        b.set_children([c])
        c.set_children([d])
        d.set_children([e])
        e.set_children([a])
        self.assertEqual(route_between_nodes_iterative(a, c), True)

