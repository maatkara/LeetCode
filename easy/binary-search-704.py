import numpy as np
import pytest

string_ = """
704. Binary Search
https://leetcode.com/problems/binary-search/
Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------------
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
----------------
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
----------------
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are **unique**.
nums is sorted in ascending order.

Time complexity: O(log n)
Space complexity: O(n)

06.01.23
"""
N_MAX = int(2e4)
N_MIN = 1

A_MAX = int(1e4)
A_MIN = -int(1e4)


def search(nums: list[int], target: int) -> int:

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


test_data = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([1], 4, -1),
    ([1], 1, 0),

]

f_l = [search]


@pytest.mark.parametrize('nums, target, expected', test_data)
def test(nums: list[int], target: int, expected: int):
    for f in f_l:
        ans = f(nums, target)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        arr = np.random.randint(A_MIN, A_MAX, size=n).tolist() if n > 1 else []
        target = randint(0, n + 5)

        return arr, target

    print_time(f_l, get_args, n_iter)


"""
TIME:
          min      mean     max
===================================
search  1.6e-06  2.5e-06  3.7e-06
===================================

"""
# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Binary search'
    file_name = "binary-search-704.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
