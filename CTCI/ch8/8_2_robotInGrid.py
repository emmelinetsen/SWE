import unittest

# find path for robot from top left to bottom right
# subproblem would be starting from the next position after the top left

def robotInGrid(graph):
    return determine_path(0, 0, graph, [])


def determine_path(i, j, graph, path):
    if i >= len(graph) or j >= len(graph[i]):  # if out of bounds
        return
    if graph[i][j] == 1:  # reached an invalid field
        return
    if i == len(graph) - 1 and j == len(graph[i]) - 1:  # if reached the end
        path.append([i, j])
        return path
    path.append([i,j]) # add result to path
    return determine_path(i + 1, j, graph, path) or determine_path(i, j + 1, graph, path)

class Test(unittest.TestCase):
    def test_grid_singular(self):
        grid = [[0]]
        self.assertEqual([[0,0]], robotInGrid(grid))

    def test_grid_oneRow(self):
        grid = [[0, 0, 0]]
        self.assertEqual([[0,0], [0,1], [0,2]], robotInGrid(grid))

    def test_grid_oneRow_invalid(self):
        grid = [[0, 1, 0]]
        self.assertEqual( None , robotInGrid(grid))

    def test_grid_multiRow_someInvalidFields(self):
        grid = [[0, 1, 0],
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0]]
        self.assertEqual( [[0,0], [1,0], [1,1], [1,2], [2,2], [3,2]] , robotInGrid(grid))

    def test_grid_multiRow_allValidFields(self):
        grid = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.assertEqual( [[0,0], [1,0], [2,0], [3,0], [3,1], [3,2]] , robotInGrid(grid))

if __name__ == "__main__":
    Test.main()


