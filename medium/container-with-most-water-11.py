import pytest

string_ = """
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Medium

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
------------------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
------------------
Input: height = [1,1]
Output: 1

Constraints:
------------------
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

18.9.22
"""
N_MAX = int(2e5)
N_MIX = 2
A_MAX = int(1e4)
A_MIN = 0


def max_area(height: list) -> int:
    n = len(height)
    ans = 0
    l, r = 0, n - 1

    while l < r:
        ans = max(ans, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans


test_data = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
]

f_l = [max_area]


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
=====================================
max_area  6.2e-03  6.4e-03  6.9e-03
"""
# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'
    file_name = 'container-with-most-water-11.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
