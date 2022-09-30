import heapq

import pytest

string_ = """
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city 
when viewed from a distance. 
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where 
buildings[i] = [lefti, righti, heighti]:

-lefti is the x coordinate of the left edge of the ith building.
-righti is the x coordinate of the right edge of the ith building.
-heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate 
in the form [[x1,y1],[x2,y2],...]. 
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, 
which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. 
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
 For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; 
 the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:
--------------------

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
218merged.img
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points 
in the output list.

Example 2:
--------------------
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 
Constraints:
--------------------
1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.

30.9.22
"""
N_MAX = int(1e4)
N_MIX = 1

A_MIN = -2 ** 31
A_MAX = 2 ** 31 - 1


def get_skyline(buildings: list) -> list:
    ans = [[0, 0]]
    heap = [(0, float('inf'))]  # neg_h, r

    print('\n', buildings)
    buildings = sorted([(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for _, r, _ in buildings])
    print(buildings)

    for l, neg_h, r in buildings:

        while l >= heap[0][1]:
            heapq.heappop(heap)

        if neg_h:
            heapq.heappush(heap, (neg_h, r))

        max_h = -heap[0][0]
        if max_h != ans[-1][1]:
            ans.append([l, max_h])

    ans.pop(0)
    return ans


test_data = [
    ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
     [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]),
    ([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])
]

f_l = [get_skyline]


@pytest.mark.parametrize('buildings, expected', test_data)
def test(buildings, expected):
    for i, f in enumerate(f_l):
        ans = f(buildings)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIX, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                            min      mean     max
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Heap'
    file_name = 'the-skyline-problem-218.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
