import random

import pytest

string_ = """
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
15.10.23
"""
N_MIN = 0
N_MAX = int(1e5)
A_MAX = int(1e9)
A_MIN = int(1e-9)


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums = set(nums)
    an, ans = 1, 1

    for num in nums:
        if num + 1 in nums and num - 1 not in nums:  # start point consecutive sequence
            next = num + 1
            while next in nums:
                next += 1
                an += 1
            ans = max(ans, an)
            an = 1

    return ans


a = list(range(-5, 5)) + list(range(8, 15))
random.shuffle(a)

test_data = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([9], 1),
    ([9, 9], 1),
    (list(range(5)) + list(range(8, 15)), 7),
    (a, 10),
    ([0, -1], 2),
    ([1, 0, -1], 3),
    ([], 0)

]

f_l = [longest_consecutive]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: bool):
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

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                        min      mean     max
================================================
longest_consecutive  4.7e-05  6.1e-03  1.7e-02
================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'contains-duplicate-ii-219.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
