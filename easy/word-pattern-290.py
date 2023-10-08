import random
import string

import pytest

string_ = """
290. Word Pattern
https://leetcode.com/problems/word-pattern/description/
Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

08.10.23
"""
N_MIN = 1
N_MAX = int(3e4)
A_MAX = int(1e4)
A_MIN = 1


def word_pattern(pattern: str, s: str) -> bool:
    s = s.split()

    if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
        return False

    seen = {}

    for p, w in zip(pattern, s):
        if p not in seen:
            seen[p] = w
        elif seen[p] != w:
            return False

    return True


test_data = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog dog dog dog", False),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),

    ('a', 'dog', True)
]

f_l = [word_pattern]


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
        n1: int = random.randint(N_MIN, n // 4)
        n -= n1
        m: int = N_MAX // 10 if i == n_iter - 1 else random.randint(N_MIN, N_MAX // 10)

        s: list = random.choices(string.ascii_lowercase, k=n) + [' '] * n1
        random.shuffle(s)

        s: str = ''.join(s)
        p = ''.join(random.choices(string.ascii_lowercase, k=m))

        return p, s

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
    file_name = 'word-pattern-290.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
