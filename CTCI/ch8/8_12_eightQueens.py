def eightQueens(num_rows):
    chess = [["."] * num_rows for _ in range(num_rows)]

    col_used = []
    positive_diag = []
    negative_diag = []
    res = []
    def backtrack(row, grid):
        if row == len(grid): # completed the entire board
            copy = ["".join(r) for r in grid]
            res.append(copy)
            # res.append(grid) # how come when using this, the results do not come out correctly?
            return

        for col in range(len(grid[row])):
            # check whether is valid selection
            if col in col_used or (row+col) in positive_diag or (row-col) in negative_diag:
                continue

            # if it's a valid selection, add the queen into the grid
            grid[row][col] = "Q"
            col_used.append(col)
            positive_diag.append(row + col)
            negative_diag.append(row - col)

            backtrack(row+1, grid)

            col_used.remove(col)
            positive_diag.remove(row+col)
            negative_diag.remove(row-col)
            grid[row][col] = "."

        return res



    return backtrack(0, chess)

if __name__ == "__main__":
    print(eightQueens(8))

