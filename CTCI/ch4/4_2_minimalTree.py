class BSTNode:
    def __init__(self, val):
        self.val = val
        self.leftNode = None
        self.rightNode = None

# minimalTree takes a sorted_arr as input and returns a BSTNode for the root of the BST tree.
def minimalTree(sorted_arr):

    if len(sorted_arr) == 1:
        return BSTNode(sorted_arr[0])
    if len(sorted_arr) == 0:
        return
    # get the middle value of the sorted_arr
    mid = int(len(sorted_arr)/2)
    node = BSTNode(sorted_arr[mid])
    node.leftNode = minimalTree(sorted_arr[:mid])
    node.rightNode = minimalTree(sorted_arr[mid+1:])
    return node


def printTree(root):
    if root is None:
        return
    leftVal = None
    if root.leftNode is not None:
        leftVal = root.leftNode.val
    rightVal = None
    if root.rightNode is not None:
        rightVal = root.rightNode.val
    print("root = " + str(root.val) + " left = " + str(leftVal) + " right = " + str(rightVal))
    printTree(root.leftNode)
    printTree(root.rightNode)

if __name__ == "__main__":
    # printTree(minimalTree([1,2,3]))
    printTree(minimalTree([1,2,3,4]))

    # arr = [1,2]
    # mid = int(len(arr)/2)
    # print(arr[mid+1:])
