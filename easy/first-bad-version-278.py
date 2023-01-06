import pytest

string_ = """
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
Easy

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
------------------------
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
------------------------
Input: n = 1, bad = 1
Output: 1
 
Constraints:
------------------------
1 <= bad <= n <= 2^31 - 1

Time complexity: O(log n)
Space complexity: O(1)

06.01.23
"""
N_MAX = 2 ** 31 - 1
N_MIN = 1

A_MAX = int(1e4)
A_MIN = -int(1e4)


def is_bad_version(version: int, target: int) -> bool:  # only for testing
    return version >= target


def first_bad_version(n: int, target: int) -> int:  # target only for testing
    """ Return the left l and  right r indexes in d:
        d = [0,...0, 1, 1,...] - ascending sorted( not descending)
        Invariant: d[l] < x <= d[r], x=1 (i.c. True, and there is d[l] == x)
        """

    l, r = 0, n  # l = 0 for all 1 (all bad)

    while r - l > 1:
        mid = r - (r - l) // 2

        if is_bad_version(mid, target):  # == 1
            r = mid
        else:
            l = mid

    return r


test_data = [
    (5, 4, 4),
    (1, 1, 1),
    (100, 1, 1),
    (100, 100, 100),
    (N_MAX, 2, 2),
    (N_MAX, 1, 1),
    (N_MAX, N_MAX, N_MAX),
]

f_l = [first_bad_version]


@pytest.mark.parametrize('nums, target, expected', test_data)
def test(nums: int, target: int, expected: int):
    for f in f_l:
        ans = f(nums, target)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        target = 2 if i == n_iter - 1 else randint(1, n)

        return n, target

    print_time(f_l, get_args, n_iter)


"""
TIME:
                     min      mean     max
==============================================
first_bad_version  2.4e-06  4.6e-06  2.1e-05
==============================================

"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Binary search'
    file_name = "first-bad-version-278.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
