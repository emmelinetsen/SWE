import unittest

# given real # between 0 and 1, print the binary representation
# if the # can't be represented in binary with at most 32 characters, print ERROR

# in order to get the binary representation of a decimal real # , need to multiply the decimal real # by 2
# determine whether that number is <1 or >1
def binaryToString(input_num):
    res = ["0."]

    while input_num != 0:
        # print(input_num, " ", len(res))
        if len(res) == 33: # when binary representation is over 32 characters. 33 because first value is 0. in the arr
            raise Exception ("Error. Exceed max number of characters")

        tmp = input_num * 2
        if tmp >= 1:
            res.append("1")
            input_num = tmp - 1
        else:
            res.append("0")
            input_num = tmp
    return "".join(res)


class Test(unittest.TestCase):
    def test_valid_decimal(self):
        num = 0.625
        self.assertEqual("0.101",binaryToString(num))

    def test_valid_decimal_2(self):
        num = 0.25
        self.assertEqual("0.01",binaryToString(num))

    def test_valid_decimal_exception(self):
        num = 0.75
        self.assertRaises(Exception, binaryToString(num))

if __name__ == "__main__":
    Test.main()