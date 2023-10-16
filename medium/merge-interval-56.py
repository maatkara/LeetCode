import random

import pytest

string_ = """
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/
Medium

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

16.10.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e4)
A_MIN = 0


def merge(intervals: list[list[int]]) -> list[list[int]]:

    intervals.sort(key=lambda x: x[0])
    prev = intervals[0]
    i, j = 1, len(intervals)

    while i < j:
        cur = intervals[i]
        if cur[0] <= prev[1]:
            intervals.pop(i)
            intervals[i - 1] = [prev[0], max(cur[1], prev[1])]
            prev = intervals[i - 1]
            j -= 1
        else:
            i += 1
            prev = cur

    return intervals


test_data = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 3], [0, 6], [8, 10], [15, 18]], [[0, 6], [8, 10], [15, 18]]),
    ([[1, 3], [2, 6], [8, 10], [1, 18]], [[1, 18]]),
    ([[1, 3], [2, 6], [0, 10], [1, 18]], [[0, 18]]),
    ([[1, 3], [2, 6], [1, 10], [0, 0]], [[0, 0], [1, 10]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4]], [[1, 4]])
]

f_l = [merge]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[list[int]], expected: list[list[int]]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        nums1: list = np.random.randint(A_MIN, A_MAX, size=n).tolist()
        nums2: list = np.random.randint(A_MIN, A_MAX, size=n).tolist()
        nums1.sort()
        nums2.sort()

        return [sorted((c1, c2)) for c1, c2 in zip(nums1, nums2)],

    print_time(f_l, get_args, n_iter)


"""
TIME:
         min      mean     max
==================================
merge  7.8e-05  3.2e-03  1.2e-02
==================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Intervals'
    file_name = 'summary-ranges-228.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
