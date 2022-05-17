import unittest


def parens(num):
    return parens_map(num, [])


def parens_map(num, m):
    if num <= 0:
        return []

    if num == 1 and "()" not in m:
        m.append("()")
        return ["()"]
    if num == 2:
        res = []
        if "()()" not in m:
            m.append("()()")
            res.append("()()")
        if "(())" not in m:
            m.append("(())")
            res.append("(())")
        return res

    res = []
    for i in range(3,num+1):
        perm = parens_map(num-1, m) # getting the different permutations from n-1
        for p in perm:
            # need to account for outside paren, l/r paren
            outside = "(" + p + ")"
            left = "()" + p
            right = p + "()"
            # add the resulting parenthesis if not already accounted for
            if outside not in m:
                m.append(outside)
                res.append(outside)
            if left not in m:
                m.append(left)
                res.append(left)
            if right not in m:
                m.append(right)
                res.append(right)
    return res


class Test(unittest.TestCase):
    def test_parens(self):
        self.assertEqual(["(()())", "()()()", "((()))", "()(())", "(())()"], parens(3))

    def test_parens_1(self):
        self.assertEqual(["()"], parens(1))

    def test_parens_2(self):
        self.assertEqual(["()()", "(())"], parens(2))


if __name__ == "__main__":
    Test.main()
