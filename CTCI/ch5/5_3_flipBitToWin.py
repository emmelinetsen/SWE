import unittest

def flipBitToWin(number):
    bin_num = bin(number)[2:]
    max_ones, ones, prev = 0, 0, 0
    hasZero = False
    anyZeros = False


    for i in range(len(bin_num)):
        if bin_num[i] == "1":
            ones += 1
        else:
            anyZeros = True
            if hasZero and bin_num[i-1] == 0: # if previous value had zero and there's already a zero
                hasZero = False
                prev = 0
            elif hasZero:
                hasZero = False
                max_ones = max(max_ones, ones + prev)
                prev = ones
                ones = 0
            elif not hasZero:
                hasZero = True
                max_ones = max(max_ones, ones + prev)
                prev = ones
                ones = 0
    return max(max_ones, ones + prev) + 1 if anyZeros else max(max_ones, ones + prev)

class Test (unittest.TestCase):
    def test_flipBitToWin_oneZeroInBetween(self):
        self.assertEqual(8, flipBitToWin(1775)) #11011101111

    def test_flipBitToWin_multipleZerosInBetween(self):
        self.assertEqual(9, flipBitToWin(7270910)) #11011101111000111111110

    def test_flipBitToWin_noZeros(self):
        self.assertEqual(4, flipBitToWin(15)) #1111



if __name__ == "__main__":
    Test.main()