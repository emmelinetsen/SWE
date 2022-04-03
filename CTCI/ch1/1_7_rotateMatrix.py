def rotateMatrix(matrix):
    numLayers = len(matrix)/2
    for layer in range(numLayers):
        for i in range(len(matrix)):
            # swap
            tmp = matrix[i][len(matrix)-1]
            matrix[i][len(matrix)-1] = matrix[layer, i]
            matrix[layer, i] = matrix[len(matrix)-i][layer]
            matrix[len(matrix)-i][layer] = matrix[len(matrix)-layer][len(matrix)-i]
            matrix[len(matrix)-layer][len(matrix)-i] = tmp
    return matrix

if __name__ == '__main__':
    print(rotateMatrix([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16]]))