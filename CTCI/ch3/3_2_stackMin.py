import math
import unittest

# learn how to use collections instead of creating another class
class StackValue:
    def __init__(self, value, current_min):
        self.value = value
        self.min = min(current_min, value)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append(StackValue(value, math.inf))
        else:
            # s = self.stack[-1]
            self.stack.append(StackValue(value, self.stack[-1].min))

    def min(self):
        return self.stack[-1].min

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Exception: Empty stack.")
        self.stack.pop()

    def return_stack(self):
        arr = []
        for i in self.stack:
            arr.append(i.value)
        return arr

class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push(5)
        s.push(2)
        self.assertEqual(s.return_stack(), [5, 2])

    def test_min(self):
        s = Stack()
        s.push(3)
        s.push(1)
        s.push(4)
        s.push(2)
        self.assertEqual(s.min(), 1)

    def test_pop(self):
        s = Stack()
        s.push(5)
        s.push(2)
        s.pop()
        self.assertEqual(s.return_stack(), [5])

    def test_pop_empty_stack(self):
        s = Stack()
        s.push(5)
        s.push(2)
        s.pop()
        s.pop()
        with self.assertRaises(Exception):
            s.pop()

if __name__ == "__main__":
    unittest.main()
