import random

import pytest

string_ = """
202. Happy Number
https://leetcode.com/problems/happy-number/description/
Easy

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 2^31 - 1

15.10.23
"""
N_MIN = 1
N_MAX = 2 ** 31 - 1
A_MAX = int(1e4)
A_MIN = 1


def is_happy(n: int) -> bool:
    seen = set()
    h = [i ** 2 for i in range(10)]

    def helper(s):
        if s == 1 or s == 7:
            return True

        if s not in seen:
            seen.add(s)
            summ = sum([h[int(c)] for c in str(s)])
            return helper(summ)
        return False

    return helper(n)


test_data = [
    (19, True),
    (2, False)
]

f_l = [is_happy]


@pytest.mark.parametrize('t, expected', test_data)
def test(t: int, expected: bool):
    for f in f_l:
        ans = f(t)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        return n,

    print_time(f_l, get_args, n_iter)


"""
TIME:
            min      mean     max
=====================================
is_happy  6.4e-06  2.5e-05  1.1e-04
=====================================
 
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'happy-number-202.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
