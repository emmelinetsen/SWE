import unittest
from queue import Queue

class Node:
    def __init__(self, node):
        self.node = node
        self.dependencies = []
        self.incoming_dependencies = 0


class Project:
    projects = {}

    def __init__(self, arr):
        self.add_projects(arr)

    # first find projects with no dependencies
    # add those projects into a queue
    # when removing projects from queue, add project resulting array and add the children with no dep
    # keep iterating queue until there are no more values
    def buildOrder(self):
        q = Queue()
        res = []
        # find projects with no dependencies and add projects into queue
        for project, node in self.projects.items():
            if node.incoming_dependencies == 0:
                q.put(node)
        if q.empty():
            raise Exception("Cycle exists.")

        while not q.empty():
            proj = q.get()
            res.append(proj.node)
            # add children with no dependencies
            for dependency in proj.dependencies:
                dependency.incoming_dependencies -= 1
                if dependency.incoming_dependencies == 0:
                    q.put(dependency)

        return res

    def add_projects(self, arr):
        # print(arr)
        for i in arr:
            # i[0] is the project
            # i[1] is dependent on i[0]

            if i[0] not in self.projects:
                self.projects[i[0]] = Node(i[0])
            if i[1] not in self.projects:
                self.projects[i[1]] = Node(i[1])

            # add dependency to node
            project = self.projects[i[0]]
            dependency = self.projects[i[1]]
            project.dependencies.append(dependency)
            dependency.incoming_dependencies += 1

    def print_projects(self, arr):
        for i in arr:
            print(i.node)


class Test(unittest.TestCase):
    def setUp(self):
        Project.projects = {}

    def test_add_projects(self):
        dep = [["a", "d"], ["f", "b"], ["f", "a"]]
        p = Project(dep)


    def test_buildOrder(self):
        dep = [["a", "d"], ["f", "a"]]
        p = Project(dep)
        # p.print_projects(p.buildOrder())
        self.assertEqual(["f", "a", "d"], p.buildOrder())

    def test_buildOrder_cycle(self):
        dep = [["a", "d"], ["d", "a"]]
        p = Project(dep)
        # p.print_projects(p.buildOrder())
        with self.assertRaises(Exception):
            p.buildOrder()
