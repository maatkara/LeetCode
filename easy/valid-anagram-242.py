import random
import string
from collections import Counter, defaultdict

import pytest

string_ = """
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: 
What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?

09.10.23
"""
N_MIN = 1
N_MAX = int(5e4)
A_MAX = int(1e4)
A_MIN = 1


def is_anagram(s: str, t: str) -> bool:  # submitted
    if len(s) != len(t):
        return False

    s = Counter(s)
    t = Counter(t)

    if len(s) != len(t):
        return False

    for k in s:
        if k not in t or t[k] != s[k]:
            return False
    return True


def is_anagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    h = defaultdict(int)

    for ch1, ch2 in zip(s, t):
        h[ch1] += 1
        h[ch2] -= 1

    return all(v == 0 for v in h.values())


test_data = [
    ("anagram", "nagaram", True),
    ("anag ram", "nag aram", True),
    ("rat", "car", False),
    ("rate", "carr", False),
    ("r at", "car r", False),
    ("raat", "char", False),
    ("car", "car", True),
    ("carr", "ccar", False),
    ("ccarr", "ccaar", False)
]

f_l = [is_anagram, is_anagram1]


@pytest.mark.parametrize('t, nums, expected', test_data)
def test(t: str, nums: str, expected: bool):
    for f in f_l:
        ans = f(t, nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)

        s = ''.join(random.choices(string.ascii_lowercase, k=n))
        t = ''.join(random.choices(string.ascii_lowercase, k=m))

        return s, t

    print_time(f_l, get_args, n_iter)


"""
TIME:
                min      mean     max
=========================================
word_pattern  1.2e-06  4.9e-05  2.1e-04
=========================================
 
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'valid-anagram-242.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
