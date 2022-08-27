import random
import time

import pytest

"""
78. Subsets
https://leetcode.com/problems/subsets/
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
N_MAX = 10
A_MAX = 10


def subset(nums: list) -> list:
    ans_ = [[]]
    n = len(nums)

    for i in range(n):
        ans_ += [subset + [nums[i]] for subset in ans_]

    return ans_


def subset_rec(nums: list) -> list:
    ans = []
    n = len(nums)

    def dfs(i: int, subset: list) -> int:

        ans.append(subset)

        if i < n:
            for j in range(i, n):
                dfs(j + 1, subset + [nums[j]])

    dfs(0, [])

    return ans


def subset_bitmask(nums: list) -> list:
    ans = []
    n = len(nums)

    for i in range(2 ** n, 2 ** (n + 1)):
        bitmask = bin(i)[3:]  # bitmask, from 0..00 to 1..11
        ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return ans


test_data = [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),

]
f_l = [subset, subset_rec, subset_bitmask]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums, expected):
    for f in f_l:
        print('\n', f.__name__)
        for it in f(nums):
            assert it in expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for _ in range(n_iter):
        nums = list(range(-N_MAX, N_MAX))
        random.shuffle(nums)
        nums = nums[:N_MAX]

        for i, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(nums)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)

    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])


"""
   subset           0.038052334000894916
   subset_rec       0.0003553299993654946
   subset_bitmask   0.0015050509991851868

"""
