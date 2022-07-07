import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        # set the head of the tree
        self.root = Node("")

    # returns T/F for whether the word is stored in the Trie
    # starting with the first character of the word and root node, determine whether children of root node
    # contain first character.
    # if yes, continue
    # if no, return false
    # if at the end of the word, return true
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word
        # return True

    # start with the root node as the starting node and start with the first char of the word
    # check whether the character is a child of the current node
    # if yes, move current node to be the child node
    # if no, create a new node with that character. set the new node to be a child of the current node.
    # set char to be the next character
    def insert(self, word):
        node = self.root
        # start with the first character of the word
        for char in word:
            if char in node.children: # if the character is in the children of the current node, continue
                node = node.children[char]
            else: # else insert new node as child of the current node
                node.children[char] = Node(char)
                node = node.children[char]
        node.is_word = True

class Test(unittest.TestCase):
    def test_search_was_T(self):
        t = Trie()
        t.insert("was")
        self.assertEqual(t.search("was"), True)

    def test_search_was_F(self):
        t = Trie()
        t.insert("war")
        self.assertEqual(t.search("was"), False)

    def test_search_bb(self):
        t = Trie()
        t.insert("b")
        self.assertEqual(t.search("bb"), False)

    def test_search_b(self):
        t = Trie()
        t.insert("bb")
        self.assertEqual(t.search("b"), False)


if __name__ == "__main__":
    unittest.main()