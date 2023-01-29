import random

import pytest

string_ = """
268. Missing Number
https://leetcode.com/problems/missing-number/
Easy

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
----------------------
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
----------------------
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
----------------------
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.
 
Constraints:
----------------------
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

29.01.23
"""
N_MAX = int(1e4)
N_MIN = 1

A_MAX = N_MAX
A_MIN = 0


def missing_number(nums: list[int]) -> int:
    """ TC O(n) SC = O(1) """
    nums = set(nums)

    for i in range(len(nums) + 1):
        if i not in nums:
            return i

    return -1


def missing_number1(nums: list[int]) -> int:  # sub
    """ TC O(n) SC = O(1) - arithmetic progression, S=(a1+an)*n/2 """
    n = len(nums)
    return int(n * (n + 1) / 2) - sum(nums)


ns = [num for num in range(A_MIN, N_MAX) if num != 5]

test_data = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    (ns, 5)
]

f_l = [missing_number, missing_number1]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: int):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        out = randint(A_MIN, n)
        nums = [num for num in range(A_MIN, n + 1) if num != out]
        random.shuffle(nums)

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                   min      mean     max
============================================
missing_number   4.9e-06  2.2e-04  1.4e-03
missing_number1  2.0e-06  3.1e-05  9.4e-05
============================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array, Math'

    file_name = 'missing-number-268.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
