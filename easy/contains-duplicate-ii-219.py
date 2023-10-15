import random

import pytest

string_ = """
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/
Easy

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

15.10.23
"""
N_MIN = 1
N_MAX = int(1e5)
A_MAX = int(1e9)
A_MIN = int(1e-9)


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False


test_data = [
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 0, -1, -1], 1, True),
    ([-1, 0, 1, -1], 1, False),
    ([1, 2, 3, 1, 2, 3], 2, False),
    ([-1, 2, -3, 1, 2, 3], 2, False)
]

f_l = [contains_nearby_duplicate]


@pytest.mark.parametrize('nums, k, expected', test_data)
def test(nums: list[int], k: int, expected: bool):
    for f in f_l:
        ans = f(nums, k)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        k: int = N_MAX if i == n_iter - 1 else random.randint(0, N_MAX)

        nums: list = np.random.randint(A_MIN, A_MAX, size=n).tolist()

        return nums, k

    print_time(f_l, get_args, n_iter)


"""
TIME:
======================================================
contains_nearby_duplicate  1.3e-04  3.7e-03  1.7e-02
======================================================
 
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'contains-duplicate-ii-219.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
