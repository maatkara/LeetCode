import random

import pytest

string_ = """
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
Medium

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] 
denotes a balloon whose horizontal diameter stretches between xstart and xend. 
You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
 There is no limit to the number of arrows that can be shot. 
 A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1

19.10.23
"""
N_MIN = 1
N_MAX = int(1e5)
A_MAX = 2 ** 31
A_MIN = -2 ** 31


def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    end = points[0][1]  # -float('inf')
    count = 1

    for lo, hi in points[1:]:
        if end < lo:  # нет пересечения
            end = hi
            count += 1

    return count


def find_min_arrow_shots1(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    end = -float('inf')
    count = 0

    for lo, hi in points:
        if end < lo:  # нет пересечения
            end = hi
            count += 1

    return count


test_data = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[1, 2]], 1),
    ([[1, 2], [1, 2]], 1),
    ([[10, 16], [2, 8], [1, 6], [7, 12], [12, 12]], 2),
    ([[10, 16], [2, 8], [1, 6], [7, 12], [16, 16]], 3),
    ([[-2147483646, -2147483645], [2147483646, 2147483647]], 2),
    ([[2, 3], [2, 3]], 1),
    ([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]], 2)

]

f_l = [find_min_arrow_shots1, find_min_arrow_shots]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[list[int]], expected: int):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        nums: list = np.random.randint(A_MIN, A_MAX, size=2 * n).tolist()
        nums = [[nums[i], nums[i + 1]] for i in range(len(nums)) if not i % 2]

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                         min      mean     max
==================================================
find_min_arrow_shots1  7.0e-05  3.0e-02  7.1e-02
find_min_arrow_shots   1.6e-05  2.4e-02  6.1e-02
==================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Intervals'
    file_name = 'minimum-number-of-arrows-to-burst-balloons-452.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
