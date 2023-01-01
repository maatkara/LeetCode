import pytest

string_ = """
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
Easy

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
------------------
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
------------------
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
------------------
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
------------------
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


Time complexity: O(n)
Space complexity: O(1)
01.01.23
"""
N_MAX = int(1e4)
N_MIN = 1

A_MIN = -int(1e3)
A_MAX = int(1e3)


def pivot_index(nums: list[int]) -> int:  # submitted
    l_sum = 0
    s = sum(nums)

    for i, num in enumerate(nums):

        if l_sum == s - num - l_sum:
            return i
        l_sum += num

    return -1


def pivot_index1(nums: list[int]) -> int:  # submitted
    l_sum = 0
    r_sum = sum(nums)
    nums = [0] + nums

    for i in range(1, len(nums)):
        l_sum += nums[i - 1]
        r_sum -= nums[i]

        if l_sum == r_sum:
            return i - 1

    return -1


test_data = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),

    ([2], 0),
    ([0] * N_MAX, 0),
    ([A_MAX] * (N_MAX - 1), N_MAX // 2 - 1),
    ([A_MIN] * (N_MAX - 1), N_MAX // 2 - 1),
]

f_l = [pivot_index, pivot_index1]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums, expected):
    for i, f in enumerate(f_l):
        ans = f(nums)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)

        return [randint(a_min, a_max) for _ in range(n)].copy(),

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 1e4
TIME:
                min      mean     max
=========================================
pivot_index   1.1e-06  4.5e-04  1.1e-03
pivot_index1  1.2e-06  5.1e-04  1.2e-03
=========================================

O(n) ~ 1e-4
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = "find-pivot-index-724.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
