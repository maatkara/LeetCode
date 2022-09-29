import pytest

string_ = """
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
Medium

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
--------------------------
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
--------------------------
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:
--------------------------
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4

29.9.22
"""
N_MAX = int(1e4)
N_MIX = 1

A_MIN = -int(1e4)
A_MAX = int(1e4)


def find_closest_elements(arr: list, k: int, x: int) -> list:
    def key_f(ai):
        return abs(ai - x)

    arr.sort(key=key_f)

    return sorted([arr[i] for i in range(k)])


def find_closest_elements_bs(arr: list, k: int, x: int) -> list:
    l = 0
    r = len(arr) - k

    while l < r:
        mid = l + (r - l) // 2

        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid

    return [arr[i] for i in range(l, l + k)]


test_data = [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, 6, [2, 3, 4, 5]),
    ([0, 2, 3, 4, 6], 4, 3, [0, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ([0, 2, 3, 4, 6], 5, 3, [0, 2, 3, 4, 6]),
    ([0, 2, 3, 4, 6], 1, 3, [3]),

]

f_l = [find_closest_elements, find_closest_elements_bs]


@pytest.mark.parametrize('arr, k, x, expected', test_data)
def test(arr, k, x, expected):
    for i, f in enumerate(f_l):
        ans = f(arr.copy(), k, x)
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
=====================================================
find_closest_elements     1.7e-04  1.8e-04  2.3e-04
find_closest_elements_bs  2.1e-05  2.2e-05  3.9e-05
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Binary search'
    file_name = 'find-k-closest-elements-658.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
