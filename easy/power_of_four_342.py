import sys

from math import log2
from math import floor
import pytest
import random
import time

"""
342. Power of Four
https://leetcode.com/problems/power-of-four/
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
 

Constraints:
-2^31 <= n <= 2^31 - 1
 
Follow up: Could you solve it without loops/recursion?
22.08.22
"""

N_MAX = int(1e3)
A_MAX = 2 ** 31
T_MAX = 0.1


def is_power_of_four(n) -> bool:
    """ If log(n, base=4) is an integer -> True"""
    if n <= 0:
        return False
    n_log4 = log2(n) / log2(4)
    return n_log4 == floor(n_log4)


test_data = [
    (16, True),
    (0, False),
    (1, True),
    (5, False),
    (2 ** 30, True),
    (2 ** 30 + 1, False),
    (-(2 ** 30), False),
    (-(2 ** 31), False),
]


@pytest.mark.parametrize('n, expected', test_data)
def test(n, expected):
    f = is_power_of_four
    assert f(n) == expected


