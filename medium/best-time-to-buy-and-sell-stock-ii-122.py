import random

import pytest

string_ = """
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:
--------------
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
--------------
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
--------------
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:
--------------
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4

28.07.23
"""
N_MIN = 1
N_MAX = int(3e4)
A_MAX = int(1e4)
A_MIN = 0


def max_profit(prices: list[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        if delta > 0:
            profit += delta

    return profit


def max_profit1(prices: list[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


def max_profit2(prices: list[int]) -> int:
    return sum([(prices[i] - prices[i - 1]) for i in range(1, len(prices)) if prices[i] > prices[i - 1]])


test_data = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([0], 0),
    ([1], 0),

]

f_l = [max_profit, max_profit1, max_profit2]  #


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, nums)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
               min      mean     max
========================================
max_profit   1.8e-05  1.5e-03  5.4e-03
max_profit1  1.7e-05  1.6e-03  5.7e-03
max_profit2  1.9e-05  1.5e-03  5.6e-03
========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'best-time-to-buy-and-sell-stock-ii-122.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
