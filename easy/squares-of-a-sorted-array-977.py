import random

import pytest

string_ = """
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
Easy

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
--------------------
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
--------------------
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:
--------------------
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
 

Follow up: 
Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?

24.07.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e4)
A_MIN = -A_MAX


def sorted_squares(nums: list[int]) -> list[int]:
    ans, negs = [], []
    i, n = 0, len(nums)

    while i < n and nums[i] < 0:
        negs.append(nums[i] ** 2)
        i += 1

    j = i
    while j < n and i:
        cur = negs[i - 1]
        num_cur = nums[j] ** 2

        if cur < num_cur:
            ans.append(cur)
            i -= 1
        else:
            ans.append(num_cur)
            j += 1

    while i:
        ans.append(negs[i - 1])
        i -= 1

    while j < n:
        ans.append(nums[j] ** 2)
        j += 1
    return ans


test_data = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([0, 0, 0], [0, 0, 0]),
    ([0, 1, 2], [0, 1, 4]),
    ([-2, -1], [1, 4]),
    ([-2, -1, 0], [0, 1, 4]),
    ([6], [36]),
    ([-6], [36]),
]

f_l = [sorted_squares]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from random import randint

    from utils.print_time4random import print_time
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        nums = random.choices(list(range(A_MIN, A_MAX)), k=n)
        # random.shuffle(nums)

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                  min      mean     max
===========================================
sorted_squares  1.2e-05  1.2e-03  3.6e-03
===========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'squares-of-a-sorted-array-977.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
