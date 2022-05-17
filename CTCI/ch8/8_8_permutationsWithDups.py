import unittest


# compute all permutations of string whose characters are not necessarily unique
# list of permutations should not have any dups

def permutations(s):
    return permutations_map(s, [])

def permutations_map(s, m):
    # find all permutations for a string
    # add the value into the map
    # if it's in the map, don't add that string
    if len(s) <= 1 and s not in m:
        m.append(s)
        return [s]

    if len(s) == 2:
        res = []
        if s not in m:
            res.append(s)
            m.append(s)
        str = s[1] + s[0]
        if str not in m:
            res.append(str)
            m.append(str)
        return res

    res = []
    for idx, char in enumerate(s):
        perm = permutations_map(s[0:idx] + s[idx+1:], m)
        for p in perm:
            str = char + p
            if str not in m:
                res.append(str)
                m.append(str)
    return res





class Test(unittest.TestCase):
    def test_permutations(self):
        s = "abc"
        res = ["abc", "acb", "bac", "bca", "cab", "cba"]
        self.assertEqual(res, permutations(s))

    def test_permutations_2(self):
        s = "abb"
        res = ["abb", "bab", "bba"]
        self.assertEqual(res, permutations(s))

    def test_permutations_2chars(self):
        s = "ab"
        res = ["ab", "ba"]
        self.assertEqual(res, permutations(s))

    def test_permutations_1char(self):
        s = "a"
        self.assertEqual(["a"], permutations(s))


if __name__ == "__main__":
    Test.main()