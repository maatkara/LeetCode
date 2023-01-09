import numpy as np
import pytest

string_ = """
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
------------------
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
------------------
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:
------------------
2 <= cost.length <= 1000
0 <= cost[i] <= 999

Time complexity: O(n)
Space complexity: O(1)  min_cost_climbing_stairs_space, O(n)  min_cost_climbing_stairs, 

09.01.23
"""
N_MAX = int(1e3)
N_MIN = 2
A_MAX = 999
A_MIN = 0


def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    assert n > 1, f'len(cost) must be positive, got {n}'

    d = [-1] * (n + 1)
    d[0] = cost[0]
    d[1] = cost[1]
    cost += [0]  # add 'top'

    for i in range(2, n + 1):
        d[i] = min(d[i - 1], d[i - 2]) + cost[i]

    return d[n]


def min_cost_climbing_stairs_space(cost: list[int]) -> int:
    """ Memory efficient"""
    n = len(cost)
    assert n > 1, f'len(cost) must be positive, got {n}'

    prev = cost[0]
    cur = cost[1]
    cost += [0]  # add 'top'

    for i in range(2, n + 1):
        prev, cur = cur, min(prev, cur) + cost[i]

    return cur


test_data = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([1, 5], 1),
    ([5] * 10, 25),
    ([5] * 11, 25),
    ([5] * 3, 5),
    ([0] * 3, 0),
    ([0] * 5, 0),
    ([5] * 5, 10),
]

f_l = [min_cost_climbing_stairs, min_cost_climbing_stairs_space]


@pytest.mark.parametrize('cost, expected', test_data)
def test(cost: list[int], expected: int):
    for f in f_l:
        ans = f(cost)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        cost = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()

        return cost,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                                  min      mean     max
===========================================================
min_cost_climbing_stairs        2.0e-06  1.1e-04  2.1e-04
min_cost_climbing_stairs_space  1.4e-06  7.7e-05  1.8e-04 sub
===========================================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Dp'
    file_name = 'min-cost-climbing-stairs-746.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
