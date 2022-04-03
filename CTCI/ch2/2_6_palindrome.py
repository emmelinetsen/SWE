import unittest

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    head = None
    tail = None

    def __init__(self, arr):
        self.head = self.tail = Node()
        for i in arr:
            self.append(i)

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end=',')
            ptr = ptr.next

    def palindrome(self, ll):
        s = []
        ptr1 = ptr2 = ll.head.next
        if ptr1 is None:
            return False

        while ptr1 is not None:
            s.append(ptr1.value)
            ptr1 = ptr1.next
        while ptr2 is not None:
            num = s.pop()
            if num != ptr2.value:
                return False
            ptr2 = ptr2.next
        return True

    # def reverseList(self, ll):
    #     if ll.head.next is None:
    #         return ll.head
    #     prev, curr, following = None,  ll.head, ll.head.next
    #     while curr:
    #         curr.next = prev
    #         prev = curr
    #         curr = following
    #     return prev

class TestLinkedList(unittest.TestCase):
    def test_isPalindrome(self):
        ll = LinkedList(['a', 'b', 'c', 'b', 'a'])
        self.assertEqual(ll.palindrome(ll), True)

    def test_isNotPalindrome(self):
        ll = LinkedList(['a', 'b', 'c', 'b', 'c'])
        self.assertEqual(ll.palindrome(ll), False)

    def test_palindrome_1Value(self):
        ll = LinkedList(['a'])
        self.assertEqual(ll.palindrome(ll), True)

    def test_palindrome_noValues(self):
        ll = LinkedList([])
        self.assertEqual(ll.palindrome(ll), False)
