import unittest

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

    def getSize(self):
        return len(self.__stack)

    def return_stack(self):
        return self.__stack


class Queue:
    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack() # Queue


    def add(self, val):
        while self.__stack2.getSize() > 0: # adding values from stack2 into stack1
            self.__stack1.push(self.__stack2.pop())

        self.__stack1.push(val)

        while self.__stack1.getSize() > 0: # pushing values from stack1 into stack2
            self.__stack2.push(self.__stack1.pop())

    def remove(self):
        return self.__stack2.pop()

    def peek(self):
        s = self.__stack2.return_stack()
        return s[-1]

    def isEmpty(self):
        return len(self.__stack2) == 0

    def return_queue(self):
        return self.__stack2.return_stack()

class TestQueue(unittest.TestCase):
    def test_add(self):
        q = Queue()
        for i in range(5):
            q.add(i)
        self.assertEqual(q.peek(), 0)
        self.assertEqual(q.return_queue(), [4,3,2,1,0])

    def test_remove(self):
        q = Queue()
        for i in range(5):
            q.add(i)
        q.remove()
        q.remove()
        self.assertEqual(q.peek(), 2)

    def test_add_remove(self):
        q = Queue()
        for i in range(5):
            q.add(i)
        for i in range(2):
            q.remove()
        for i in range(3):
            q.add(i)
        self.assertEqual(q.return_queue(), [2,1,0,4,3,2])