import random
import time

import pytest

"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
Easy
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the customer i has in the j bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
25.08.22
"""

N_MAX = 50
X_MAX = 100


def maximum_wealth(accounts: list) -> int:
    return max([sum(row) for row in accounts])


def maximum_wealth1(accounts: list) -> int:
    return max(map(sum, accounts))


test_data = [
    ([[1, 2, 3], [3, 2, 1]], 6),
    ([[1]], 1),
    ([[1, 1, 1]], 3),
    ([[1], [1], [1]], 1),
    ([[1, 5], [7, 3], [3, 5]], 10),
    ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17)
]


@pytest.mark.parametrize('num, expected', test_data)
def test(num, expected):
    for f in [maximum_wealth, maximum_wealth1]:  #
        print('\n', f.__name__)
        assert f(num) == expected


def test_time(n_iter: int = 1):  # 00):
    f_l = [maximum_wealth, maximum_wealth1]
    acc = [0] * len(f_l)
    for _ in range(n_iter):
        r = random.randint(1, N_MAX)
        c = random.randint(1, N_MAX)
        accounts = [[random.randint(1, X_MAX) for row in range(1, r + 1)] for _ in range(1, c + 1)]
        print(r, c, accounts)

        for i, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(accounts)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)

    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])  # 6.881000444991514e-06


"""
"""
