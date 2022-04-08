class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def append(self, child):
        self.children.append(child)

    def addNodes(self, arr):
        for i in arr:
            self.children.append(i)

if __name__ == "__main__":

    a = Node("5")
    b = Node("3")
    c = Node("4")
    d = Node("2")

    # b.append(a)
    # d.append(b)
    # d.append(c)
    b.addNodes([a])
    d.addNodes([b,c])

    graph = Graph([a,b,c,d])
    print(graph)

    # only possible with unique vertices
    adj_list = {
        "3": ["2", "4"],
        "5": ["1", "6"]
    }