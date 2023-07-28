import random

import pytest

string_ = """
189. Rotate Array
https://leetcode.com/problems/rotate-array/
Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
-------------------
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
-------------------
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
-------------------
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 

Follow up:

- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

28.07.23
"""
N_MIN = 1
N_MAX = int(1e5)
A_MAX = 1 ** 31 - 1
A_MIN = -A_MAX - 1


def rotate(nums: list[int], k: int, verbose=False) -> None:
    if verbose: print(id(nums))
    if k > len(nums):
        k %= len(nums)
    if not k:
        return
    nums[:] = nums[-k:] + nums[:-k]
    if verbose: print(id(nums))


def rotate1(nums: list[int], k: int, verbose=False) -> None:
    if verbose: print(id(nums))
    if k >= len(nums):
        k %= len(nums)

    if not k:
        return

    item = [0] * k

    for i in range(k):
        item[i] = nums.pop()

    nums[:] = nums[::-1]
    nums.extend(item)
    nums[:] = nums[::-1]
    if verbose: print(id(nums))


def rotate2(nums: list[int], k: int, verbose=False) -> None:
    """ Inplace, SC=O(1)"""
    if verbose: print(id(nums))

    def rev(lst: list[int], n: int, m: int):
        """ In-place reverse list from n to m included"""
        j = m
        mid = n + (m - n + 1) // 2

        for i in range(n, mid):
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1

    if k >= len(nums):
        k %= len(nums)

    if not k:
        return

    rev(nums, 0, len(nums) - 1)
    rev(nums, 0, k - 1)
    rev(nums, k, len(nums) - 1)
    if verbose: print(id(nums))


def rotate3(nums: list[int], k: int, verbose=False) -> None:
    """ Inplace, SC=O(1)"""

    def rev(lst: list[int], n: int, m: int):
        """ In-place reverse list from n to m (NOT included)"""
        j = m - 1

        for i in range(n, n + (m - n) // 2):
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1

    if k >= len(nums):
        k %= len(nums)

    if not k:
        return

    rev(nums, 0, len(nums))
    rev(nums, 0, k)
    rev(nums, k, len(nums))


test_data = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([-1, -100, 3, 99, 101], 3, [3, 99, 101, -1, -100]),
    ([-1, -100, 3, 99], 6, [3, 99, -1, -100]),
    ([1], 5, [1]),
    (list(range(100)), 100 - 1, list(range(1, 100)) + [0]),
    (list(range(8)), 7, list(range(1, 8)) + [0])
]

f_l = [rotate, rotate1, rotate2, rotate3]  #


@pytest.mark.parametrize('nums, k, expected', test_data)
def test(nums: list[int], k: int, expected: list[int]):
    for f in f_l:
        nums1 = nums.copy()
        f(nums1, k)
        print('\n', f.__name__, nums1)

        assert nums1 == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        k: int = N_MAX if i == n_iter - 1 else random.randint(0, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()

        return nums, k

    print_time(f_l, get_args, n_iter)


"""
TIME:
           min      mean     max
====================================
rotate   1.1e-05  3.6e-04  1.1e-03
rotate1  1.1e-06  1.5e-03  5.8e-03
rotate2  1.5e-06  4.3e-03  1.1e-02
rotate3  5.9e-07  4.3e-03  8.1e-03
====================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'rotate-array-189.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
