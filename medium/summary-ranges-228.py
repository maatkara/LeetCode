import random

import pytest

string_ = """
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/description/
Easy

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.

16.10.23
"""
N_MIN = 0
N_MAX = 20
A_MAX = 2 ** 31
A_MIN = -2 ** 31


def summary_ranges(nums: list[int]) -> list[str]:
    if not nums:
        return []

    prev = nums[0]
    an, ans = str(prev), []

    for num in nums[1:] + [nums[-1] + 2]:
        if num - 1 != prev:  # start point consecutive sequence
            an += '->' + str(prev) if int(an) != prev else ''
            ans.append(an)
            an = str(num)
        prev = num
    return ans


test_data = [
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 1, 2, 4, 5, 6], ["0->2", "4->6"]),
    ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ([0], ["0"]),
    ([], []),
    ([-2147483648, -2147483647, 2147483647], ['-2147483648->-2147483647', '2147483647'])
]

f_l = [summary_ranges]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[str]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        nums: list = np.random.randint(A_MIN, A_MAX, size=n).tolist()

        return nums.sort(),

    print_time(f_l, get_args, n_iter)


"""
TIME:
                  min      mean     max
===========================================
summary_ranges  1.9e-07  2.4e-07  1.1e-06
===========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Intervals'
    file_name = 'summary-ranges-228.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
