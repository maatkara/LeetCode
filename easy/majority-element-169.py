from collections import Counter

import pytest

string_ = """
169. Majority Element
https://leetcode.com/problems/majority-element/description/
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 

Example 1:
---------------------------
Input: nums = [3,2,3]
Output: 3

Example 2:
---------------------------
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
---------------------------
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

25.07.23
"""
N_MIN = 1
N_MAX = int(5e4)
A_MAX = int(1e9)
A_MIN = -A_MAX


def majority_element_naive(nums: list[int]) -> int:
    return Counter(nums).most_common()[0][0]


def majority_element(nums: list[int]) -> int:
    prev = None
    count = 0
    n = len(nums) // 2 + 1
    nums.sort()

    for num in nums:
        if num == prev:
            count += 1
            if count == n:
                return num
        else:
            count = 1
            prev = num
    return prev


def majority_element1(nums: list[int]) -> int:  # submit
    curr, count = nums[0], 1  # curr will store the current majority element, count will store the count of the majority
    for i in nums[1:]:
        # if i is equal to current majority, they're in same team, hence added,
        # else one current majority and i both will be dead
        count += (1 if curr == i else -1)

        if not count:  # if count of current majority is zero, then change the majority element, and start its count from 1
            curr = i
            count = 1
    return curr


test_data = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1], 1),
    ([-1], -1)

]

f_l = [majority_element1, majority_element, majority_element_naive]  #


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: int):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from random import randint

    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        out = [randint(A_MIN, A_MAX)] * (n // 2 + 1)
        nums = np.random.randint(A_MIN, A_MAX, n // 2, dtype=int).tolist() + out

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                          min      mean     max
===================================================
majority_element1       3.1e-05  1.5e-03  4.6e-03
majority_element        5.7e-05  2.7e-03  6.5e-03
majority_element_naive  4.9e-05  3.1e-03  1.7e-02
===================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'majority-element-169.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
