import random

import pytest

string_ = """
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
--------------------
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
--------------------
Input: nums = [1,1]
Output: [2]

Constraints:
--------------------
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
 
Follow up: 
--------------------
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

11.07.23
"""
N_MAX = int(1e5)
N_MIN = 1

A_MAX = N_MAX
A_MIN = 1


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
        For each number i in nums,
    we mark the number that i points as negative.
    Then we filter the list, get all the indexes
    that point to a positive number.
    Since those indexes are not visited.
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


test_data = [
    ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
    ([1, 1], [2]),
    (list(range(2, int(1e5)))+[2], [1])
]

f_l = [find_disappeared_numbers]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
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
=====================================================
find_disappeared_numbers  2.3e-05  1.1e-02  2.3e-02
=====================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'find-all-numbers-disappeared-in-an-array-448.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
