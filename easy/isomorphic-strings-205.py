import string
from random import choices

import pytest

string_ = """
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
-------------
Input: s = "egg", t = "add"
Output: true

Example 2:
-------------
Input: s = "foo", t = "bar"
Output: false

Example 3:
-------------
Input: s = "paper", t = "title"
Output: true
 
Constraints:
-------------
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.


Time complexity: O(n)
Space complexity: O(1)
01.01.23
"""
N_MAX = int(5e4)
N_MIN = 1


def is_isomorphic1(s: str, t: str) -> bool:  # sub
    if len(s) != len(t):
        return False

    hs = dict()
    ht = dict()

    for cs, ct in zip(s, t):
        if (cs in hs and hs[cs] != ct) or (ct in ht and ht[ct] != cs):
            return False
        hs[cs] = ct
        ht[ct] = cs

    return True


def is_isomorphic2(s: str, t: str) -> bool:
    return len(s) == len(t) and len(set(s)) == len(set(t)) == len(set(zip(s, t)))


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t) or len(set(s)) != len(set(t)):
        return False

    h = dict()

    for cs, ct in zip(s, t):
        if cs in h and h[cs] != ct:
            return False
        h[cs] = ct

    return True


test_data = [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),

    ('a', 'b', True),
    ('aa', 'a', False),
    ('Aa', 'aa', False),
    ('aa', 'Aa', False),
    ('abra', 'bddr', False),
    ('bddr', 'abra', False),
    ('abracadabra', 'aebaeadaeba', False),
    ('hhhhhhaab', 'hhhhhcccd', False),
    ('a' * N_MAX, 'd' * N_MAX, True),
    (string.ascii_letters, string.ascii_letters, True),
    (string.ascii_letters, ''.join(string.ascii_letters.split()[::-1]), True),
]

f_l = [is_isomorphic, is_isomorphic1, is_isomorphic2]


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
                 n_max: int = N_MAX, a_max: int = None,
                 n_min: int = N_MIN, a_min: int = None) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        s = ''.join(choices(string.ascii_letters, k=n))
        t = ''.join(choices(string.ascii_letters, k=n)) if i != n_iter - 1 else s

        return s, t

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 1e4
TIME:
                  min      mean     max
===========================================
is_isomorphic   1.1e-05  5.6e-04  5.1e-03
is_isomorphic1  9.1e-07  8.4e-05  8.2e-03 sub
is_isomorphic2  7.7e-06  1.9e-03  5.7e-03
===========================================

O(n) ~ 1e-4
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String, Hash'
    file_name = "isomorphic-strings.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
