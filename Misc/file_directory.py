# https://leetcode.com/discuss/interview-experience/1379020/Google-phone-screen
# given a file directory as a string in following way, print the path as a tree

# input:
# '/a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2'
#
# output:
# a
# -c
# --ac
# --ac2
# -b
# --ab
# b
# -c
# --bc
from collections import OrderedDict

class Tree:
    def __init__(self):
        self.directory_paths = dict()

    # in: an array containing the order of the file
    # out: no output
    # go through each partition, while also determining whether it's in the directory paths?
    def add(self, partitions):
        curr = self.directory_paths
        for partition in partitions:
            if partition not in curr:
                curr[partition] = dict()
            curr = curr[partition]

    def print(self):
        print(self.directory_paths.items())

def print_path(paths):
    # parse the array and store the paths into an array
    # add the path into the tree
    t = Tree()
    for path in paths:
        if path[0] == '/': # starts with path directory
            directories = path[1:].split('/')
        else:
            directories = path.split('/')
        t.add(directories)

        print(directories)
    t.print()

if __name__ == "__main__":
    print_path(['/a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2'])