import random
import string

import pytest

string_ = """
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Easy

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.

8.08.23
"""

N_MAX = int(1e4)
N_MIN = 1


def str_str(haystack: str, needle: str) -> int:
    w = len(needle)

    if len(haystack) < w:
        return -1

    i = 0
    while i <= len(haystack) - w:
        j = 0
        while j < w and haystack[i + j] == needle[j]:
            j += 1

        if j == w:
            return i
        else:
            i += 1

    return -1


test_data = [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("leetcode", 'cod', 4),
    ('camel', 'l', 4),
    ('camel', 'camelot', -1),

]

f_l = [str_str]


@pytest.mark.parametrize('s, s1, expected', test_data)
def test(s, s1, expected):
    for f in f_l:
        ans = f(s, s1)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m = random.randint(N_MIN, n)

        s = ''.join(random.choices(string.ascii_lowercase, k=n))
        s1 = ''.join(random.choices(string.ascii_lowercase, k=m))

        return s, s1

    print_time(f_l, get_args, n_iter)


"""
           min      mean     max
====================================
str_str  1.9e-06  5.5e-04  2.2e-03
====================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'find-the-index-of-the-first-occurrence-in-a-string-28.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
