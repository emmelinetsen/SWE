# sort a stack such that the smallest items are on the top
# can use additional temp stack, but no additional data structures
# the stack supports push, pop, peek, isEmpty
import math
import random
import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def sort(self):
        # tmp = Stack()
        res = Stack()
        stack_len = len(self.stack)

        for i in range(stack_len):
            stack_max = self.pop()
            while not self.isEmpty():
                top = self.pop()
                if top > stack_max:  # update the max value to top
                    tmp.push(stack_max)
                    stack_max = top
                else:
                    tmp.push(top)
            res.push(stack_max)
            tmp2 = self
            self = tmp
            tmp = tmp2
        self.stack = res
        return self.stack

    def sort2(self):
        tmp = Stack()
        stack_len = len(self.stack)
        for i in range(stack_len):
            stack_max = self.pop()
            for j in range(stack_len - i - 1):
                top = self.pop()
                if top > stack_max:
                    tmp.push(stack_max)
                    stack_max = top
                else:
                    tmp.push(top)
            self.push(stack_max)
            while not tmp.isEmpty():
                self.push(tmp.pop())

    def sort3(self):
        tmp = Stack()
        while not self.isEmpty():
            val = self.pop()
            while not tmp.isEmpty() and tmp.peek() > val:
                self.push(tmp.pop())
            tmp.push(val)
        while not tmp.isEmpty():
            self.push(tmp.pop())



    def return_stack(self):
        res = []
        for i in self.stack:
            res.append(i)
        return res


class TestSort(unittest.TestCase):
    def test_sort_maxOnTopInput(self):
        s = Stack()
        val = 10
        for i in range(5):
            s.push(val + i)
        # s.sort2()
        s.sort3()
        self.assertEqual(s.return_stack(), [14, 13, 12, 11, 10])

    def test_sort(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(2)
        s.push(4)
        s.push(5)
        # s.sort2()
        s.sort3()
        self.assertEqual(s.return_stack(), [5, 4, 3, 2, 1])
        self.assertEqual(s.peek(), 1)

    def test_sort_sameNumbers(self):
        s = Stack()
        for i in range(5):
            s.push(1)
        # s.sort2()
        s.sort3()
        self.assertEqual(s.return_stack(), [1,1,1,1,1])

    def test_sort_1Number(self):
        s = Stack()
        s.push(1)
        # s.sort2()
        s.sort3()
        self.assertEqual(s.return_stack(), [1])
