# implement a binary search tree class from scratch
# implement an insert, find, delete, and getRandomNode() method which returns a random node from a tree

from queue import Queue
import random

class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.left_node_count = 0
        self.right_node_count = 0

    def getRandomNode(self):
        total_nodes = self.left_node_count + self.right_node_count + 1
        if total_nodes == 1:
            return self

        rand = random.randint(1,total_nodes)
        if rand == self.left_node_count + 1:
            return self
        if 1 <= rand <= self.left_node_count:
            return self.left.getRandomNode()
        elif self.left_node_count + 2 <= total_nodes:
            return self.right.getRandomNode()



    def delete(self, num_node):
        # put the bottom most right leaf node from the deleted node to the position where the node is being deleted
        node = self.find(num_node)
        leaf = self.leaf_node(node)

        self.decrease_node_counts(leaf)

        # remove the leaf node from the bottom of the tree
        if leaf.parent.left == leaf:
            leaf.parent.left = None
        else:
            leaf.parent.right = None

        # if deleting the leaf node, return
        if leaf == node:
            return

        node.val = leaf.val
        # # updating the node counts
        # leaf.left_node_count = node.left_node_count
        # leaf.right_node_count = node.right_node_count
        #
        # # updating the left and right nodes of leaf
        # leaf.left = node.left
        # leaf.right = node.right
        #
        # if node.parent.left == node:
        #     node.parent.left = leaf
        # elif node.parent.right == node:
        #     node.parent.right = leaf

        # swap/bubble the values down the tree
        while not self.valid_bst(node):
            # swap the nodes accordingly
            # update the left and right node count
            self.swap(node)


    def swap(self, node):
        if node.val < node.left.val:
            tmp = node.val
            node.val = node.left.val
            node.left.val = tmp
        elif node.val > node.right.val:
            tmp = node.val
            node.val = node.right.val
            node.right.val = tmp


    def valid_bst(self, node):
        if node.left and node.right:
            return node.left.val <= node.val < node.right.val
        if node.left:
            return node.left.val <= node.val
        if node.right:
            return node.val < node.right.val

    # gets the most right leaf node
    # if there is no right node, then gets the left node
    def leaf_node(self, node):
        while node.right:
            node = node.right
        if node.left:
            return node.left
        return node


    def insert(self, new_node):
        # compare new node value with self and move left or right depending on where the node should be when there is
        # a position where there is no node, add the new node to that position and update the left/right nodes
        if new_node <= self.val:
            if self.left:
                self = self.left
                self.insert(new_node)
            else:
                n = BinarySearchTree(new_node)
                self.left = n
                n.parent = self
                self.increase_node_counts(n)

        elif new_node > self.val:
            if self.right:
                self = self.right
                self.insert(new_node)
            else:
                n = BinarySearchTree(new_node)
                self.right = n
                n.parent = self
                self.increase_node_counts(n)


    def increase_node_counts(self, node):
        while node.parent:
            if node == node.parent.left:
                    node.parent.left_node_count += 1
            else:
                node.parent.right_node_count += 1
            node = node.parent

    def decrease_node_counts(self, node):
        while node.parent:
            if node == node.parent.left:
                node.parent.left_node_count -= 1
            else:
                node.parent.right_node_count -= 1
            node = node.parent

    # implement binary search to find the node
    def find(self, value):
        if self.val == value:
            return self
        if self.val < value:
            self = self.right
            if not self:
                raise IndexError("No such value.")
            return self.find(value)
        elif self.val > value:
            self = self.left
            if not self:
                raise IndexError("No such value.")
            return self.find(value)

    def print_tree(self, root):
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.val, " ", node.left_node_count, " ", node.right_node_count)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)


if __name__ == "__main__":
    a = BinarySearchTree(10)
    a.insert(5)
    a.insert(7)
    a.insert(6)
    a.insert(15)
    a.delete(5)
    a.print_tree(a)
    print(a.getRandomNode().val)
