import pytest

string_ = """
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
Easy

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
-------------
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
-------------
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
-------------
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 
Constraints:
-------------
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

Time complexity: O(n)
Space complexity: O(1)
01.01.23
"""
N_MAX = int(1e3)
N_MIN = 1

A_MIN = -int(1e6)
A_MAX = int(1e6)


def running_sum(nums: list[int]) -> list[int]:  # submitted

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


test_data = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),

    ([2], [2]),
    ([0] * N_MAX, [0] * N_MAX),
    ([A_MAX] * N_MAX, [A_MAX * i for i in range(1, N_MAX + 1)]),
]

f_l = [running_sum]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums, expected):
    for i, f in enumerate(f_l):
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert len(ans) == len(expected)

        # for an, ex in zip(sorted(ans), sorted(expected)):
        #     assert sorted(an) == sorted(ex)
        assert ans == expected


def test_time(n_iter: int = 1000):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)

        return [randint(a_min, a_max) for _ in range(n)].copy(),

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 1e3
TIME:
               min      mean     max
========================================
running_sum  3.9e-07  4.1e-05  1.2e-04
========================================

O(n) ~ 1e-5
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = "running-sum-of-1d-array-1480.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
