from collections import defaultdict

import pytest

string_ = """
1. Two Sum
https://leetcode.com/problems/two-sum/
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
(ic nums[i] + nums[j] = target)

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
--------------------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
--------------------
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
--------------------
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
--------------------
2 <= nums.length <= 10**4
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
N_MAX = int(1e4)
N_MIN = 2

A_MIN = -int(1e9)
A_MAX = int(1e9)


def two_sum3(nums: list, target: int) -> list:  # submitted
    h = {}

    for i in range(len(nums)):
        cur = nums[i]
        added = target - cur

        if added in h:
            return [h[added], i]
        h[cur] = i
    return [-1]


def two_sum(nums: list, target: int) -> list:
    h = {}
    hi = defaultdict(list)

    for i, k in enumerate(nums):
        h[k] = target - k
        if len(hi[k]) <= 1:
            hi[k].append(i)

    for i in range(len(nums)):
        num1 = h[nums[i]]

        if num1 in h:
            j = hi[num1][-1]

            if j != i:
                return [i, j]

    return [-1]


def two_sum0(nums: list, target: int) -> list:
    h = {}

    for i, k in enumerate(nums):
        if k not in h:
            h[k] = (target - k, [i])
        elif len(h[k][1]) == 1:
            h[k][1].append(i)

    for i in range(len(nums)):
        num1 = h[nums[i]][0]

        if num1 in h:
            j = h[num1][1][-1]

            if j != i:
                return [i, j]

    return [-1]


def two_sum1(nums: list, target: int) -> list:
    h = {}
    for i, k in enumerate(nums):
        if k not in h:
            h[k] = (target - k, [i])
        elif len(h[k][1]) == 1:
            h[k][1].append(i)

    for num in h:
        num1 = h[num][0]

        if num1 in h:
            i = h[num][1][0]
            j = h[num1][1][-1]

            if j != i:
                return [i, j]

    return [-1]


def two_sum2(nums: list, target: int) -> list:
    h = {}
    hi = defaultdict(list)

    for i, k in enumerate(nums):
        h[k] = target - k
        if len(hi[k]) <= 1:
            hi[k].append(i)

    for num in h:
        num1 = h[num]

        if num1 in h:
            i = hi[num][0]
            j = hi[num1][-1]

            if j != i:
                return [i, j]

    return [-1]


test_data = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 3, 3], 6, [0, 1]),

    ([3, -3, 3], 0, [0, 1]),
    ([3, -3, 3, 1], -2, [1, 3]),
    ([2, 2, 2], 6, [-1]),
    ([2, 2, 3, 3], 6, [2, 3]),

    ([0] * 10, 2, [-1]),
    ([0] * (N_MAX - 2) + [1, 1], 2, [N_MAX - 2, N_MAX - 1]),
    ([A_MIN] * (N_MAX // 2 - 1) + [A_MAX] * (N_MAX // 2 - 1) + [1, 1], 2, [N_MAX - 2, N_MAX - 1]),
    (list(range(2, N_MAX)) + [1, 1], 2, [N_MAX - 2, N_MAX - 1]),  # max time: 4 mc
]

f_l = [two_sum, two_sum0, two_sum1, two_sum2, two_sum3]


@pytest.mark.parametrize('nums, target, expected', test_data)
def test(nums, target, expected):
    for i, f in enumerate(f_l):
        ans = f(nums, target)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIN, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
            min      mean     max
=====================================submitted
two_sum   3.6e-03  5.0e-03  1.6e-02
two_sum0  3.0e-03  5.3e-03  1.6e-02
two_sum1  2.8e-03  5.3e-03  1.6e-02
two_sum2  3.5e-03  4.9e-03  1.6e-02
two_sum3  1.0e-03  1.1e-03  1.3e-03  submitted
=====================================

O(n^2) = 1e-9 * N_MAX**2 = 1e-1 
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'two-sum-1.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
