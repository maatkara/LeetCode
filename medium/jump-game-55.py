import random

import pytest

string_ = """
55. Jump Game
https://leetcode.com/problems/jump-game/
Medium

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
 

Example 1:
--------------------
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
--------------------
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:
--------------------
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
29.07.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e5)
A_MIN = 0


def can_jump(nums: list[int]) -> bool:
    reach_ind = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if nums[i] + i >= reach_ind:
            reach_ind = i
    return reach_ind == 0


test_data = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
]

f_l = [can_jump]  #


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
=====================================
can_jump  2.4e-06  3.1e-04  6.0e-04
=====================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'jump-game-55.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
