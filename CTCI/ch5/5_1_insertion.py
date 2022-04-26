import unittest

def bit_not(n, numbits=4):
    # print(bin(1<<numbits))
    # print(bin((1 << numbits) - 1))
    # print(bin((1 << numbits) - 1 - n))
    return (1 << numbits) - 1 - n


# insert m into n such that m starts at bit j and ends at bit i
# clear out the values between i to j. update that bit by bit?
# left shift m by i and AND with n
def insertion(n, m, i, j):
    binary = bin(n)[2:] # get the binary value without the '0b' in the front
    length = len(binary) # get the length of the binary value
    right_ones = (1 << (i)) - 1
    left_ones = (1 << (length - (i + j - 1))) - 1
    left_mask = left_ones << (i + j - 1)
    mask = right_ones | left_mask
    cleared = n & mask # need to remember to set this to clear the values in n with the mask

    return cleared | m << i

class Test (unittest.TestCase):
    def test_insertion(self):
        n = 0b10000011100
        m = 0b10011
        i = 2
        j = 6
        self.assertEqual(bin(0b10001001100), bin(insertion(n,m,i,j)))

    def test_insertion_2(self):
        n = 0b10000000
        m = 0b01
        i = 0
        j = 1
        self.assertEqual(bin(0b10000001), (bin(insertion(n,m,i,j))))


if __name__ == "__main__":
    m = 0b001
    # print(bin(bit_not(m,4)))
    # print(bin(insertion(0b10000000000, 0b10011, 2, 6)))
    Test.main()
