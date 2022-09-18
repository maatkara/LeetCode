import pytest

string_ = """
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can max_area after raining.

Example 1:
--------------
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
--------------
Input: height = [4,2,0,3,2,5]
Output: 9
 
Solution:
Minimum of maximum height of bars on both the sides minus its own height
This task is similar to medium 11 Container With Most Water: 
[Python](https://github.com/maatkara/LeetCode/blob/main/medium/container-with-most-water-11.py)


Constraints:
--------------
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

18.9.22
"""
N_MAX = int(2e4)
N_MIX = 1
A_MAX = int(1e5)
A_MIN = 0


def trap(height: list) -> int:
    """ Time O(n), Space O(1) """
    l, r = 0, len(height) - 1
    l_max, r_max = height[l], height[r]
    ans = 0

    while l < r:

        if l_max <= r_max:
            ans += (l_max - height[l])
            l += 1
            l_max = max(l_max, height[l])
        else:
            ans += (r_max - height[r])
            r -= 1
            r_max = max(r_max, height[r])

    return ans


test_data = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([4, 2, 0, 3, 2, 2], 4),
    ([4, 2, 0, 3, 3, 2], 4),
    ([4, 2, 0, 3, 2, 2, 3], 6),
    ([4, 2, 0, 3, 2, 2, 4], 11),
    ([4, 2, 0, 3, 2, 2, 4, 2, 0, 3, 2, 5], 11 + 9),
    (list(range(20)), 0),
    (list(range(20))[::-1], 0),
    ([0] * 10, 0),
    ([1] + [0] * 10 + [1], 10),
    ([1], 0)
]

f_l = [trap]


@pytest.mark.parametrize('height, expected', test_data)
def test(height: list, expected):
    for i, f in enumerate(f_l):
        ans = f(height)
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
=================================
trap  3.5e-03  3.6e-03  3.8e-03
"""
# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'
    file_name = 'trapping-rain-water_42.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
