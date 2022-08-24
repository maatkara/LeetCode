from math import log2

import pytest

"""
326. Power of Three
https://leetcode.com/problems/power-of-three/
Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true
 

Constraints:
-2^31 <= n <= 2^31 - 1
 
Follow up: Could you solve it without loops/recursion?

24.08.22
"""

A_MAX = 2 ** 31
T_MAX = 0.1


def is_power_of_three(n) -> bool:
    """ If log(n, base=3) is an integer -> True"""

    eps = 1e-9
    return n > 0 and log2(n) / log2(3) * 10 % 10 < eps


test_data = [
    (27, True),
    (0, False),
    (1, True),
    (5, False),
    (9, True),
    (3 ** 15 + 1, False),
    (3 ** 15 - 1, False),
    (-(3 ** 15), False),
    (-(2 ** 31), False),
    ((2 ** 30 + 1), False),
    (129140164, False),
    (3 ** 18 + 2, False),
    (3 ** 18 + 1, False),
    (3 ** 18 - 2, False),
    (3 ** 18 - 1, False),
    (3 ** 18, True)
]


@pytest.mark.parametrize('n, expected', test_data)
def test(n, expected):
    f = is_power_of_three
    assert f(n) == expected
