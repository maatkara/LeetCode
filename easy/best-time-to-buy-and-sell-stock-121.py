from random import randint

import pytest

string_ = """
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
-----------------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
-----------------
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
-----------------
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4


Time complexity: O(n),
Space complexity: O(1)

04.01.23
"""
N_MAX = int(1e5)
N_MIN = 1
A_MAX = int(1e4)
A_MIN = 0


def max_profit(prices: list[int]) -> int:
    profit = 0
    p_min = prices[0]

    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - p_min)
        p_min = min(p_min, prices[i])

    return profit


a_l = [randint(A_MIN, A_MAX) for _ in range(N_MAX)]
test_data = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),

    ([1], 0),
    (list(range(1, A_MAX)), A_MAX - 2),
    (list(range(1, A_MAX)) + [5] * (N_MAX-A_MAX), A_MAX - 2),
    (list(range(A_MAX, 0, -1)) + [5] * (N_MAX-A_MAX), 5 - 1),
]

f_l = [max_profit]


@pytest.mark.parametrize('prices, expected', test_data)
def test(prices: list, expected: int) -> bool:
    for i, f in enumerate(f_l):
        ans = f(prices)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN,
                 ) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        arr = np.random.randint(a_min, a_max, size=n).tolist()

        return arr,

    print_time(f_l, get_args, n_iter)


"""
TIME:
              min      mean     max
=======================================
max_profit  8.7e-05  9.9e-03  2.5e-02
=======================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Greedy'
    file_name = "best-time-to-buy-and-sell-stock-121" + ".py"

    print('\n')
    print(get_readme(string_, topic, file_name))
