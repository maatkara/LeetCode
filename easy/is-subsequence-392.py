import string
from random import choices

import pytest

string_ = """
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
-----------------
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
-----------------
Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:
-----------------
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, 
and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?

Time complexity: O(n)
Space complexity: O(1)
01.01.23
"""
N_MAX = int(1e4)
N_MIN = 0
K_MAX = int(1e2)
K_MIN = 0


def is_subsequence(s: str, t: str) -> bool:
    """ Two pointer O(n)"""
    k, n = len(s), len(t)
    if k == 0:
        return True
    if k > n:
        return False

    i, j = 0, 0  # s, t

    while j < n and i < k:
        i += s[i] == t[j]
        j += 1

    return i == k


test_data = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),

    ("", "ahbgdc", True),
    ("", "", True),
    ("ahbgdc", "", False),
    ("ahbgdc", "ahbgdc", True),
    ("ahbgdcd", "ahbgdc", False),

    ('a', 'ab', True),
    ('aa', 'abb', False),
    ('abra', 'bddr', False),
    ('abra', 'abracadabra', True),
    ('cadabra', 'abracadabra', True),
    ('hhhhhh', 'hhhhhcccd', False),
    (string.ascii_letters, string.ascii_letters, True),
    (string.ascii_letters, string.ascii_letters[::-1], False),
    (string.ascii_letters * (K_MAX // 26), string.ascii_letters[::-1] * (N_MAX // 26), True),
]

f_l = [is_subsequence]


@pytest.mark.parametrize('s, t, expected', test_data)
def test(s, t, expected):
    for i, f in enumerate(f_l):
        ans = f(s, t)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int,
                 n_max: int = N_MAX,  # a_max: int = None,
                 n_min: int = N_MIN,  # a_min: int = None,
                 k_max: int = K_MAX,
                 k_min: int = K_MIN,
                 ) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        k = k_max if i == n_iter - 1 else randint(k_min, k_max)
        t = ''.join(choices(string.ascii_lowercase, k=n))
        s = ''.join(choices(string.ascii_lowercase, k=k))

        return s, t

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 1e4
TIME:
                  min      mean     max
===========================================
is_subsequence  3.3e-06  1.2e-04  4.5e-04
===========================================
O(n) ~ 1e-4
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String, Two pointer'
    file_name = "is-subsequence-392.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
