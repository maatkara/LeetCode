'longest-repeating-character-replacement-424'
import random
import string
from collections import defaultdict

import pytest

string_ = """
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement
Medium
You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
-------------------
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
-------------------
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
-------------------
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

Time complexity: O(n)
Space complexity: O(1)

11.01.23
"""
N_MAX = int(1e5)
N_MIN = 1


def character_replacement(s: str, k: int) -> int:
    """ TC: O(n), SC:  O(1)"""
    max_len = 0
    l = 0
    freq = defaultdict(int)

    for r in range(len(s)):
        freq[s[r]] += 1
        cur_len = r - l + 1

        if cur_len - max(freq.values()) <= k:
            max_len = max(max_len, cur_len)
        else:
            freq[s[l]] -= 1
            l += 1

    return max_len


test_data = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),

    ('A', 1, 1),
    ('AAAAAA', 5, 6),
    ('ABCDFGHJ', 2, 3),
    ('ABCDFGHJA', 0, 1),
    ('ABADFGHJA', 0, 1),
    ('ABADFGHJA', 1, 3),
    ('ABADFAHJA', 2, 4),
]

f_l = [character_replacement]


@pytest.mark.parametrize('s, k, expected', test_data)
def test(s: str, k: int, expected: int):
    for f in f_l:
        ans = f(s, k)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        k = randint(0, n)
        s = ''.join(random.choices(string.ascii_uppercase, k=n))

        return s, k

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                         min      mean     max
==================================================
character_replacement  9.3e-04  3.6e-02  6.9e-02
==================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Sliding Window'
    file_name = 'find-all-anagrams-in-a-string-438.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
