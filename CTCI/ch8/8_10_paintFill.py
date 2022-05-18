import unittest


def paintFill(arr, point, new_color):
    color_at_point = arr[point[0]][point[1]]
    fill = [point]

    while fill:
        pt = fill.pop()
        row = pt[0]
        column = pt[1]

        arr[row][column] = new_color

        for i in range(row - 1, row + 2): # checking for up, down, and i
            if 0 <= i < len(arr):  # check for bounds
                for j in range(column - 1, column + 2): # checking for left, right, and j
                    if 0 <= j < len(arr[0]):  # check for bounds
                        if arr[i][j] == color_at_point:
                            fill.append([i, j])
    return arr


class Test(unittest.TestCase):
    def test_paintFill_1(self):
        screen = [[1, 1],
                  [1, 9]]
        self.assertEqual([[2, 2],
                          [2, 9]], paintFill(screen, [0,0], 2))

    def test_paintFill_2(self):
        screen = [[1, 1, 1],
                  [1, 1, 2],
                  [2, 2, 1]]
        self.assertEqual([[4, 4, 4],
                          [4, 4, 2],
                          [2, 2, 4]], paintFill(screen, [1,1], 4))

    def test_paintFill_3(self):
        screen = [[1, 1, 1],
                  [1, 1, 2],
                  [2, 2, 1]]
        self.assertEqual([[4, 4, 4],
                          [4, 4, 2],
                          [2, 2, 4]], paintFill(screen, [2,2], 4))

    def test_paintFill_4(self):
        screen = [[1, 1, 1],
                  [1, 2, 2],
                  [2, 2, 1]]
        self.assertEqual([[1, 1, 1],
                          [1, 2, 2],
                          [2, 2, 4]], paintFill(screen, [2,2], 4))


if __name__ == "__main__":
    Test.main()