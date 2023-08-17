import random
from sys import maxsize

import pytest

string_ = """
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, 
try coding another solution of which the time complexity is O(n log(n)).

14.08.23
"""
N_MIN = 1
N_MAX = int(1e5)
A_MAX = int(1e4)
A_MIN = 1


def min_sub_array_len(target: int, nums: list[int]) -> int:
    res = maxsize
    start, acc = 0, 0

    for i in range(len(nums)):
        acc += nums[i]

        while acc >= target:
            res = min(res, i - start + 1)
            acc -= nums[start]
            start += 1

    return res if res != maxsize else 0


test_data = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (1, [1], 1),
    (2, [1], 0),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    (213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], 8)

]

f_l = [min_sub_array_len]  #


@pytest.mark.parametrize('t, nums, expected', test_data)
def test(t: int, nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(t, nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()
        target = random.randint(N_MIN, int(1e9))

        return target, nums

    print_time(f_l, get_args, n_iter)


"""
TIME:
                     min      mean     max
==============================================
min_sub_array_len  1.1e-04  4.5e-03  2.0e-02
==============================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Sliding window'
    file_name = 'minimum-size-subarray-sum-209.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
