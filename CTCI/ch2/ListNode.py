class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def search_list(self, L, value):
        while L and L.value != value:
            L = L.next
        return L

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_after(self, node):
        node.next = node.next.next

class LinkedList:
    head = None
    tail = None

    def print(self):
        n = self.head
        while n is not None:
            print(n.data, end=", ")
            n = n.next
        print()
        print("head= ", self.head.data, "tail= ", self.tail.data)

    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            # node = ListNode(value)
            # self.tail.next = node
            # self.tail = node
            self.tail.next = ListNode(value)
            self.tail = self.tail.next



if __name__ == "__main__":
    # l1 = ListNode()
    # l1.insert_after(l1, ListNode(3))
    # l1.insert_after(l1.next, ListNode(4))
    # l1.insert_after(l1.next.next, ListNode(5))
    # l1.delete_after(l1)
    # while l1 is not None:
    #     print(l1.data)
    #     l1 = l1.next
    # print(l1.next.data)

    l = LinkedList()
    l.append(3)
    l.print()
    l.append(4)
    l.print()
    l.append(5)
    l.print()