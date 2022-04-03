import unittest


class SetOfStacks:
    def __init__(self):
        self.capacity = 3
        self.current_capacity = 0
        self.set_of_stacks = []
        self.set_of_stacks.append([])

    def push(self, value):
        # if self.current_capacity < self.capacity:
        if len(self.set_of_stacks[-1]) < self.capacity:
            self.set_of_stacks[-1].append(value)
            self.current_capacity += 1
        else:
            self.set_of_stacks.append([])
            self.set_of_stacks[-1].append(value)
            self.current_capacity = 1

    def pop(self):

        # if self.current_capacity > 0:
        if len(self.set_of_stacks[-1]) > 0:
            self.set_of_stacks[-1].pop()
            self.current_capacity -= 1
        else:
            if len(self.set_of_stacks) > 1: # current stack empty but there are more stacks to pop
                # self.set_of_stacks.pop()
                while len(self.set_of_stacks[-1]) == 0:
                    self.set_of_stacks.pop()
                self.set_of_stacks[-1].pop()
                self.current_capacity = self.capacity - 1
            elif len(self.set_of_stacks) <= 1: # last stack and it's empty
                raise IndexError("Exception: No values to pop.")


    def popAt(self, index):
        if index >= len(self.set_of_stacks) or index < 0:
            raise IndexError("Index Error: Invalid index.")
        if len(self.set_of_stacks[index]) == 0:
            raise IndexError("Exception: No values to pop")

        self.set_of_stacks[index].pop()


    def return_stack(self):
        return self.set_of_stacks

class Stack:
    def __init__(self):
        self.set = SetOfStacks()

    def push(self, val):
        self.set.push(val)


    def pop(self):
        self.set.pop()



class TestStack(unittest.TestCase):
    def test_stack_instantiate(self):
        s = Stack()
        # self.assertEqual(len(s.stack), 3)
        self.assertEqual(len(s.set.set_of_stacks), 1)

    def test_stack_over_capacity(self):
        s = Stack()
        s.push(1)
        s.push(1)
        s.push(1)
        s.push(1)
        # self.assertEqual(len(s.stack), 3)
        self.assertEqual(len(s.set.set_of_stacks), 2)

    def test_stack_pop_outOfCapacity_withPush(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s.pop()
        s.pop()
        s.pop()
        s.push(6)
        s.push(10)
        self.assertEqual(s.set.return_stack(), [[1,2,6],[10]])

    def test_setOfStacks_popAt(self):
        s = SetOfStacks()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s.popAt(0)
        self.assertEqual(s.return_stack(), [[1,2],[4,5]])

    def test_setOfStacks_popAt_emptyMiddleStack(self):
        s = SetOfStacks()
        for i in range(9):
            s.push(i)

        for i in range(3):
            print(s.return_stack(), "current_capacity: ", s.current_capacity)
            s.popAt(1)

        for i in range(4):
            print(s.return_stack(), "current_capacity: ", s.current_capacity)
            s.pop()

        print(s.return_stack())
        self.assertEqual(s.return_stack(), [[0,1]])

    def test_setOfStacks_popAt_noIndextoPop(self):
        s = SetOfStacks()
        for i in range(9):
            s.push(i)

        for i in range(3):
            s.popAt(1)

        with self.assertRaises(IndexError):
            s.popAt(1)

    def test_setOfStacks_popAt_noIndextoPop(self):
        s = SetOfStacks()
        for i in range(9):
            s.push(i)

        for i in range(2):
            print(s.return_stack(), "current_capacity: ", s.current_capacity)
            s.popAt(1)

        for i in range(6):
            print(s.return_stack(), "current_capacity: ", s.current_capacity)
            s.pop()

        print(s.return_stack(), "current_capacity: ", s.current_capacity)
        self.assertEqual(s.return_stack(), [[0]] )