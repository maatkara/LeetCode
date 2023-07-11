import pytest

string_ = """
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
Easy

Given an integer x, return true if x is a palindrome, and false otherwise.
 

Example 1:
-----------------
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
-----------------
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
-----------------
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-----------------
-2^31 <= x <= 2^31 - 1
 

Follow up: Could you solve it without converting the integer to a string?

11.07.23
"""

A_MAX = int(1e31) - 1
A_MIN = -A_MAX - 1


def is_palindrom(x: int) -> bool:
    if x < 0:
        return False

    new = 0
    orig = x

    while x:
        x, cur = divmod(x, 10)
        new = new * 10 + cur

    return new == orig


test_data = [
    (121, True),
    (-121, False),
    (10, False)
]

f_l = [is_palindrom]


@pytest.mark.parametrize('x, expected', test_data)
def test(x: int, expected: bool):
    for f in f_l:
        ans = f(x)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = A_MAX if i == n_iter - 1 else randint(A_MIN, A_MAX)
        return n,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                min      mean     max
=========================================
is_palindrom  1.4e-07  2.5e-06  5.8e-06
=========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Math'
    file_name = 'palindrome-number-9.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
