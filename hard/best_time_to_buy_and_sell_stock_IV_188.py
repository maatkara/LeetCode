import pytest

from utils.make_string import get_readme

string_ = """
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
--------------------------
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
--------------------------
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
--------------------------
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

10.9.22
"""
K_MAX = 100
N_MAX = int(1e3)
A_MAX = int(1e3)


def max_profit(k: int, prices: list) -> int:
    def take_all_gap():
        profit = 0
        for i in range(1, n):
            gap = prices[i] - prices[i - 1]
            profit += gap if gap > 0 else 0
        return profit

    n = len(prices)
    if k >= n // 2:  # we can every day bay or sell => all gap +
        return take_all_gap()

    dp = [[0] * n for _ in range(k + 1)]  # k+1 x n

    for i in range(1, k + 1):
        max_temp = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], max_temp + prices[j])
            max_temp = max(max_temp, dp[i - 1][j - 1] - prices[j])
    return dp[-1][-1]


def max_profit_bu(k: int, prices: list) -> int:
    """ Minimizing memory - submitted to LC"""

    def take_all_gap():
        profit = 0
        for i in range(1, n):
            gap = prices[i] - prices[i - 1]
            profit += gap if gap > 0 else 0
        return profit

    n = len(prices)
    if k >= n // 2:  # We can every day bay or sell => all gap +
        return take_all_gap()

    prev = [0] * n  # Max profit,  previous transaction
    for i in range(1, k + 1):

        min_opp_cost = prices[0]  # Min opportunity cost of a transaction
        cur = [0]  # Max profit, current transaction
        for j in range(1, n):
            cur.append(max(
                cur[-1],
                prices[j] - min_opp_cost
            ))
            min_opp_cost = min(min_opp_cost, prices[j] - prev[j - 1])
        prev = cur

    return prev[n - 1]


test_data = [
    (2, [2, 4, 1], 2),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (3, [3, 2, 6, 5, 0, 3], 7),
    (3, [3, 2, 6, 5, 0, 3, 7], 11),
    (2, [3, 2, 6, 5, 0, 3, 7], 11),
    (2, [3, 2, 6, 5, 1, 3, 7, 0, 9], 15),
    (3, [3, 2, 6, 5, 1, 3, 7, 0, 9], 19),
    (2, [1, 1, 1, 1, 1], 0),
    (4, list(range(10, -1, -1)), 0),
    (4, list(range(10, -1, -1)) + list(range(1, 10)), 9)
]
f_l = [max_profit_bu, max_profit]


@pytest.mark.parametrize('k, prices, expected', test_data)
def test(k, prices, expected):
    for i, f in enumerate(f_l):
        ans = f(k, prices)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    import random
    import time

    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(0, N_MAX)
        k = K_MAX if i == n_iter - 1 else random.randint(0, min(K_MAX, n // 2))
        prices = [random.randint(0, A_MAX) for _ in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(k, prices)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])


"""
max_profit_bu 0.03565221799908613
max_profit    0.03988179800035141
"""


# -------------------------------


# TO README
def test_readme():
    topic = 'Dp'
    file_name = 'best_time_to_buy_and_sell_stock_IV_188.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
