import unittest

def recursive_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    return recursive_multiply_bin(bin(a), bin(b))


def recursive_multiply_bin(a, b):
    bin_b = b[2:]  # only has the binary digits

    if len(bin_b) == 1: # multiplying by 1
        return int(a[2:],2)

    ones_to_shift_b = (1 << len(bin_b) - 1) - 1
    shifted_b = int(b[2:], 2) & ones_to_shift_b # remove most left digit from b
    shifted_a = int(a[2:], 2) << len(bin_b) - 1 # shift a by len(b)-1 to add

    # if b[0] is 0, a = 0, if b[0] is 1, a = a
    # shift a to the left based on the length of b
    a1 = int(bin(shifted_a)[2:], 2)
    b1 = recursive_multiply_bin(a, bin(shifted_b))
    return a1 + b1


def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

class Test(unittest.TestCase):
    def test_multiply_singledigits(self):
        self.assertEqual(15, recursive_multiply(3,5))

    def test_multiply_doubledigits(self):
        self.assertEqual(575, recursive_multiply(25, 23))

    def test_multiply_zero_1(self):
        self.assertEqual(0, recursive_multiply(0, 23))

    def test_multiply_zero_2(self):
        self.assertEqual(0, recursive_multiply(23, 0))

    def test_multiply_one_1(self):
        self.assertEqual(23, recursive_multiply(1, 23))

    def test_multiply_one_2(self):
        self.assertEqual(14, recursive_multiply(14, 1))

if __name__ == "__main__":
    Test.main()