import random

import pytest

string_ = """
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

19.10.23
"""
N_MIN = 1
N_MAX = int(1e4)


# A_MAX = 2 ** 31
# A_MIN = -2 ** 31


def is_valid(s: str) -> bool:
    if len(s) % 2:
        return False

    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif not stack or ch != pairs[stack.pop()]:
            return False
    return not stack


test_data = [
    ("()", True),
    ("())", False),
    (")", False),
    ("(", False),
    ("(]", False),
    ('([](){([])})', True),
    ('{{[()]]', False),

]

f_l = [is_valid]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: str, expected: bool):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        s = '(){}[]'

        nums: str = ''.join(random.choices(s, k=n))

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
            min      mean     max
=====================================
is_valid  1.8e-07  6.1e-07  2.9e-06
=====================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Stack'
    file_name = 'valid-parentheses-20.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
