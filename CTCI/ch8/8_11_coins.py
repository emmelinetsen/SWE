import unittest

def coins(cents): # incorrect implementation
    denom = [25, 10, 5, 1]

    def coin_change(change, arr):
        if len(arr) == 1 or change in [0, 1]:
            return 1
        if len(arr) == 0:
            return 0
        perm_count = 0

        for i in range(len(arr)):
            remaining_change = change
            if remaining_change == arr[i]:
                perm_count += 1
            while remaining_change - arr[i] > 0:
                perm_count += coin_change(remaining_change - arr[i], arr[i + 1:])
                remaining_change -= arr[i]

        return perm_count
    return coin_change(cents, denom)

def solution(coins): # correct implementation

    # coin_change_solution returns blah blah given the amount, coins, idx
    def coin_change_solution(amount, denoms, idx):
        if idx >= len(denoms) - 1: # last denom
            return 1
        denomAmount = denoms[idx]
        ways = 0
        i = 0
        while i * denomAmount <= amount: # uses the same amount to determine permutations
            remaining = amount - i * denomAmount
            ways += coin_change_solution(remaining, denoms, idx + 1)
            i += 1
        return ways

    return coin_change_solution(coins, [25, 10, 5, 1], 0)

class Test(unittest.TestCase):
    def test_coins_0(self):
        self.assertEqual(solution(0), coins(0))

    def test_coins_1(self):
        self.assertEqual(solution(1), coins(1))

    def test_coins_5(self):
        self.assertEqual(solution(5), coins(5))

    def test_coins_11(self):
        self.assertEqual(solution(11), coins(11)) # 11 pennies, 1 nickel/6 pennies, 2 nickels/ 1 penny, 1 dime/ 1 penny

    def test_coins_25(self):
        self.assertEqual(solution(25), coins(25))

if __name__ == "__main__":
    Test.main()
