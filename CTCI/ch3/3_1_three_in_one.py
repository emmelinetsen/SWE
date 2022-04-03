# single array in 3 stacks
# have 3 pointers, each representing the location of each stack
# the first position for each stack would be:
## stack1 = 0
## stack2 = 1
## stack3 = 2
# each incremental add to the stack would be stack+=3
# when the user wants to pop, just take off the value at arr[stack] and then move the ptr stack-=3

class Stack:


    def __init__(self, stack_size):
        self.__arr = [None] * (stack_size * 3)
        self.__stack = {
            "stack1": 0,
            "stack2": 1,
            "stack3": 2
        }


    def push(self, stack, value):
        pos = self.get_stack_position(stack)
        if self.is_full(pos):
            raise Exception("Stack full.")
        self.__arr[pos] = value
        self.update_stack_position_increase(stack)

    def pop(self, stack):
        pos = self.get_stack_position(stack)
        # print(self.__arr[pos - 3])
        self.update_stack_position_decrease(stack)

    def is_full(self, position):
        return position >= len(self.__arr)

    def get_stack_position(self, stack):
        return self.__stack[stack]


    def update_stack_position_increase(self, stack):
        self.__stack[stack] += 3


    def update_stack_position_decrease(self, stack):
        self.__stack[stack] -= 3


    def get_starting_stack_position(self, stack):
        if stack == "stack1":
            return 0
        if stack == "stack2":
            return 1
        if stack == "stack3":
            return 2

    def print_stack(self, stack):
        pos = self.get_starting_stack_position(stack)
        for i in range(int(len(self.__arr) / 3)):
            print(self.__arr[pos], end=" ")
            pos += 3
        print()


if __name__ == "__main__":
    s = Stack(3)
    # s.push("stack1", 1)
    # # s.print_stack("stack2")
    # s.push("stack2", 2)
    # s.push("stack1", 4)
    # s.push("stack1", 5)
    # # s.pop("stack1")
    # s.push("stack1", 8)

    # s.print_stack("stack1")
    s.push("stack3", 1)
    s.push("stack3", 1)
    # s.push("stack3", 1)
    s.push("stack3", 1)

    s.print_stack("stack3")

    s2 = Stack(3)
    s2.push("stack1", 1)
    # s2.print_stack("stack1")