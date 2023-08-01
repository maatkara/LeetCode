import random

import pytest

string_ = """
134. Gas Station
https://leetcode.com/problems/gas-station/
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique

 

Example 1:
------------------
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
------------------
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:
------------------
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4

01.08.23
"""
N_MIN = 1
N_MAX = int(1e5)
A_MAX = int(1e4)
A_MIN = 0


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    start = 0  # start point
    fund = 0
    cost[:] = [i - j for i, j in zip(gas, cost)]

    if sum(cost) < 0:
        return -1

    for i in range(len(gas)):
        fund += cost[i]
        if fund < 0:
            fund = 0
            start = i + 1

    return start


test_data = [
    ([5, 1, 2, 3, 4], [2, 3, 4, 5, 1], 4),
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([2, 1, 0, 0], [0, 1, 0, 0], 0)
]

f_l = [can_complete_circuit]  #


@pytest.mark.parametrize('nums, nums1, expected', test_data)
def test(nums: list[int], nums1: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums, nums1.copy())
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()
        nums1: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()

        return nums, nums1

    print_time(f_l, get_args, n_iter)


"""
                        min      mean     max
=================================================
can_complete_circuit  5.8e-05  5.1e-03  1.3e-02
=================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'gas-station-134.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
