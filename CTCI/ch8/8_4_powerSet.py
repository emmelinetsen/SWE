import unittest

def power_set(ps):
    res = []
    if len(ps) == 0:
        return res
    if len(ps) == 1:
        res.append([ps[0]])
        return res
    if len(ps) == 2:
        res.append([ps[0]])
        res.append([ps[1]])
        res.append([ps[0],ps[1]])
        return res

    for idx in range(len(ps)):
        subset = power_set(ps[idx+1:])
        for s in subset:
            s.append(ps[idx])
            res.append(s)
        res.append([ps[idx]])
    return res

class Test (unittest.TestCase):
    def test_power_set(self):
        powerset = [1,2,3]
        self.assertEqual([[2, 1], [3, 1], [2, 3, 1], [1], [3, 2], [2], [3]], power_set(powerset))

    def test_power_set_2_values(self):
        powerset = [1,2]
        self.assertEqual([[1], [2], [1, 2]], power_set(powerset))

    def test_power_set_1_value(self):
        powerset = [1]
        self.assertEqual([[1]], power_set(powerset))

if __name__ == "__main__":
   Test.main()