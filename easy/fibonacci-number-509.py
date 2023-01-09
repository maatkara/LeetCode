import pytest

string_ = """
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/description/
Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
-----------------
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
-----------------
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
-----------------
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
-----------------
0 <= n <= 30

Time complexity: O(n)
Space complexity: O(n)

09.01.23
"""
N_MAX = 30
N_MIN = 0


def fib(n: int) -> int:
    assert n >= 0, f'n must be >=0, got {n}'

    d = [0, 1] + [-1] * (n - 1)

    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


test_data = [
    (2, 1),
    (3, 2),
    (4, 3),
    (1, 1),
    (0, 0),
    (6, 8)
]

f_l = [fib]


@pytest.mark.parametrize('n, expected', test_data)
def test(n: int, expected: int):
    for f in f_l:
        ans = f(n)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        return n,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
       min      mean     max
================================
fib  3.9e-07  1.6e-06  3.9e-06
================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Dp'
    file_name = 'fibonacci-number-509.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
