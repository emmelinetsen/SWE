import unittest


# compute all permutations of a string of unique characters
def permutations(s):
    res = []
    if len(s) <= 1:
        return [s]
    if len(s) == 2:
        return [s, s[1] + s[0]]
    for idx, char in enumerate(s):
        perm = permutations(s[0:idx]+s[idx+1:]) # getting the string before and after the current character
        for p in perm:
            res.append(char + p)
    return res


class Test(unittest.TestCase):
    def test_permutations(self):
        s = "abc"
        self.assertEqual(["abc", "acb", "bac", "bca", "cab", "cba"], permutations(s))

    def test_permutations_2(self):
        s = "ABCD"
        self.assertEqual(["ABCD", "ABDC", "ACBD", "ACDB", "ADBC", "ADCB",
                          "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
                          "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA",
                          "DABC", "DACB", "DBAC", "DBCA", "DCAB", "DCBA"], permutations(s))

    def test_permutations_2chars(self):
        s = "ab"
        self.assertEqual(["ab", "ba"], permutations(s))

    def test_permutations_1char(self):
        s = "a"
        self.assertEqual(["a"], permutations(s))


if __name__ == "__main__":
    Test.main()
