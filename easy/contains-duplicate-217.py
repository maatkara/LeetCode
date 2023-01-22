import pytest

string_ = """
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Easy

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
-----------------------------
Input: nums = [1,2,3,1]
Output: true

Example 2:
-----------------------------
Input: nums = [1,2,3,4]
Output: false

Example 3:
-----------------------------
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
-----------------------------
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

22.01.23
"""
N_MAX = int(1e5)
N_MIN = 1

A_MAX = int(1e9)
A_MIN = -int(1e9)


def contains_duplicate(nums: list[int]) -> bool:
    """ TC O(n) SC = O(n) """
    return len(nums) != len(set(nums))


def contains_duplicate1(nums: list[int]) -> bool:
    """ TC O(n) SC = O(n) """
    h = set()

    for num in nums:
        if num in h:
            return True
        h.add(num)

    return False


test_data = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([1] * 50, True),
    (list(range(N_MIN, N_MAX)), False),

]

f_l = [contains_duplicate, contains_duplicate1]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: bool):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        nums = np.random.randint(A_MIN, A_MAX + 1, size=n, dtype=int).tolist()

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                       min      mean     max
================================================
contains_duplicate   8.1e-05  2.5e-03  7.9e-03
contains_duplicate1  1.2e-04  3.0e-03  1.1e-02
================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'

    file_name = 'contains-duplicate-217.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
