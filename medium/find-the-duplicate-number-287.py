import random

import pytest

string_ = """
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
--------------------
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
--------------------
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
--------------------
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

29.01.23
"""
N_MAX = int(1e5)
N_MIN = 1

A_MAX = N_MAX
A_MIN = 1


def find_duplicate(nums: list[int]) -> int:  # sub
    """ TC O(n) SC = O(1)  - Floyd's circle -> see 142 Linked List Cycle II """
    slow = fast = ans = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    while ans != slow:
        ans = nums[ans]
        slow = nums[slow]
    return ans


test_data = [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([1, 1], 1),
    (list(range(1, N_MAX)) + [5], 5),
    ([2, 2, 2, 2, 2], 2)
]

f_l = [find_duplicate]


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
        nums = list(range(A_MIN, n + 1)) + [out]
        random.shuffle(nums)

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                  min      mean     max
===========================================
find_duplicate  2.1e-06  4.0e-03  1.6e-02
===========================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'

    file_name = 'find-the-duplicate-number-287.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
