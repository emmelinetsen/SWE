import unittest

# t1: source
# t2: destination
# t3: buffer
def towers(n, t1, t2, t3):
    if n == 0:
        return [t1, t2, t3]
    elif n == 1:
        # move the 1 value from t1 to t2
        t2.append(t1.pop())
    elif n == 2:
        # use t3 as a buffer
        t3.append(t1.pop())
        t2.append(t1.pop())
        t2.append(t3.pop())
    else:
        towers(n-1, t1, t3, t2) # move all but the actual value into the buffer
        towers(1, t1, t2, t3)
        towers(n-1, t3, t2, t1) # move all the values from the buffer to the destination, using t1 as buffer
    return [t1, t2, t3]

class Test(unittest.TestCase):
    def test_towersOfHanoi(self):
        s1 = []
        for i in range(10,0,-1):
            s1.append(i)
        s2 = []
        s3 = []
        self.assertEqual([[],[10,9,8,7,6,5,4,3,2,1],[]], towers(len(s1), s1, s2, s3))

    def test_towersOfHanoi_move0(self):
        s1 = []
        s2 = []
        s3 = []
        self.assertEqual([[],[],[]], towers(len(s1), s1, s2, s3))

    def test_towersOfHanoi_move1(self):
        s1 = [1]
        s2 = []
        s3 = []
        self.assertEqual([[],[1],[]], towers(len(s1), s1, s2, s3))

    def test_towersOfHanoi_move2(self):
        s1 = [2,1]
        s2 = []
        s3 = []
        self.assertEqual([[],[2,1],[]], towers(len(s1), s1, s2, s3))


if __name__ == "__main__":
    Test.main()