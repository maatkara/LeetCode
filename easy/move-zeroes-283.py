import pytest

string_ = """
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/
Easy

Given an integer array nums, 
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
------------------
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
------------------
Input: nums = [0]
Output: [0]
 

Constraints:
------------------
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you minimize the total number of operations done?

27.07.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e31) - 1
A_MIN = -int(1e31)


def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] and not nums[slow]:
            nums[slow], nums[fast] = nums[fast], nums[slow]
        # wait while we find a non-zero element to
        # swap with you
        if nums[slow]:
            slow += 1


test_data = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 1, 3, 12], [1, 3, 12, 0, 0]),
    ([1, 3, 12, 0, 0, 0], [1, 3, 12, 0, 0, 0]),
    ([1, 0, 1], [1, 1, 0]),
    ([1] * 5, [1] * 5),
    ([0] * 5 + [A_MIN] * 5, [A_MIN] * 5 + [0] * 5),
    ([0] * 5 + [A_MAX] * 5, [A_MAX] * 5 + [0] * 5),
    ([0], [0])
]

f_l = [move_zeroes]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        f(nums)
        print('\n', f.__name__, nums)

        assert nums == expected


def test_time(n_iter: int = 100):
    from random import randint
    import random

    from utils.print_time4random import print_time
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        m = n // 2
        # nums = np.random.randint(A_MIN, A_MAX+1, size=(n - m), dtype=np.longlong).tolist() + [0] * m
        if n < 3:
            n = 3
        nums = [0] * m + list(range(n - m - 2)) + [A_MIN, A_MAX]
        random.shuffle(nums)

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
               min      mean     max
========================================
move_zeroes  1.3e-05  4.3e-04  9.1e-04
========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'move-zeroes-283.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
