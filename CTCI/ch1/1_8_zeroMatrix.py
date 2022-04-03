def zeroMatrix(matrix):
    zeros = set() # space complexity: O(N)
    for x in range(len(matrix)): #O(M) where M = number of rows in matrix
        y = 0
        while y < len(matrix[x]): # O(N) where N = number of columns in matrix
            if matrix[x][y] == 0:
                zeros.add(y)
                matrix[x] = [0] * len(matrix[x]) # instantiating a 0 matrix, takes up O(N) space
                y = len(matrix[x])
            else:
                y += 1

    # is it possible to update all the y values of a matrix without iterating through every row?
    for x in range(len(matrix)): #O(M)
        for z in zeros: #O(N)
            matrix[x][z] = 0

    return matrix

if __name__ == "__main__":
    # M x N matrix
    matrix = [[4,4,4],
              [0,4,4],
              [0,4,0],
              [4,4,4]]

    print(zeroMatrix(matrix))
