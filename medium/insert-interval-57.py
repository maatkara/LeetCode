import random

import pytest

string_ = """
57. Insert Interval
https://leetcode.com/problems/insert-interval/description/
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5   

17.10.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e5)
A_MIN = 0


def insert(intervals: list[list[int]],
           newInterval: list[int]) -> list[list[int]]:
    if not intervals:
        return [newInterval]
    if newInterval[0] > intervals[-1][1]:
        return intervals + [newInterval]
    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals

    lo, hi = newInterval
    i = 0

    while i < len(intervals) and lo > intervals[i][0]:
        i += 1

    if i and lo > intervals[i - 1][1] and hi < intervals[i][0]:  # строго между
        return intervals[:i] + [newInterval] + intervals[i:]

    if i and lo <= intervals[i - 1][1]:  # lo перекрывается c i-1
        i -= 1  # далее ищем правую границу i- 1
    else:  # lo перекрывается c i
        intervals[i][0] = lo  # далее ищем правую границу i

    end = i
    if hi >= intervals[-1][1]:
        intervals[end][1] = hi
        return intervals[:end + 1]

    while hi > intervals[i][1]:
        i += 1

    if hi < intervals[i][0]:
        intervals[end][1] = hi
        intervals = intervals[:end + 1] + intervals[i:]
    else:
        intervals[end][1] = intervals[i][1]
        intervals = intervals[:end + 1] + intervals[i + 1:]

    return intervals


test_data = [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 3], [6, 9]], [0, 1], [[0, 3], [6, 9]]),
    ([[2, 3], [6, 9]], [0, 1], [[0, 1], [2, 3], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 18], [[1, 2], [3, 18]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [17, 18], [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [17, 18]]),
    ([], [4, 6], [[4, 6]]),
    ([[1, 5]], [2, 3], [[1, 5]])
]

f_l = [insert]


@pytest.mark.parametrize('nums, nums1, expected', test_data)
def test(nums: list[list[int]], nums1: list[int], expected: list[list[int]]):
    for f in f_l:
        ans = f(nums, nums1)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        nums: list = np.random.randint(A_MIN, A_MAX, size=2 * n).tolist()
        nums.sort()
        nums = [nums[0]] + [nums[i] for i in range(2 * n) if i > 0 and nums[i] != nums[i - 1]]
        if len(nums) % 2:
            nums += [nums[-1] + 1]
        nums = [[nums[i], nums[i + 1]] for i in range(len(nums)) if not i % 2]

        nums1 = [random.randint(A_MIN, A_MAX), random.randint(A_MIN, A_MAX)]
        nums1.sort()

        return nums, nums1

    print_time(f_l, get_args, n_iter)


"""
TIME:
          min      mean     max
===================================
insert  7.4e-06  3.1e-04  1.5e-03
===================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Intervals'
    file_name = 'insert-interval-57.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
