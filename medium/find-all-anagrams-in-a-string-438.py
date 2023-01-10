import random
import string
from collections import defaultdict, Counter

import pytest

string_ = """
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
--------------------
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
--------------------
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
--------------------
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.

Time complexity: O()
Space complexity: O()

10.01.23
"""
N_MAX = int(3e4)
N_MIN = 1


def find_anagrams(s: str, p: str) -> list[int]:
    """ TC: O(n), SC:  O(1)"""
    n, m = len(s), len(p)
    if n < m:
        return []

    ans = []
    j = 0
    pattern = Counter(p)
    window = defaultdict(int)

    for i in range(m - 1):
        window[s[i]] += 1

    for i in range(m - 1, n):
        window[s[i]] += 1

        for ch in pattern:
            flag = window[ch] == pattern[ch]
            if not flag:
                break

        ans += [j] if flag else []
        window[s[j]] -= 1
        j += 1

    return ans


test_data = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("abaeb", "ab", [0, 1]),
    ("abab", "a", [0, 2]),
    ('b', 'a', []),
    ('ggg', 'aaaaa', [])
]

f_l = [find_anagrams]


@pytest.mark.parametrize('s, p, expected', test_data)
def test(s: str, p: str, expected: list[int]):
    for f in f_l:
        ans = f(s, p)
        print('\n', f.__name__, ans)

        assert len(ans) == len(expected)
        expected = set(expected)

        for an in ans:
            assert an in expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        m = n if i == n_iter - 1 else randint(N_MIN, n)
        s = ''.join(random.choices(string.ascii_lowercase, k=n))
        p = ''.join(random.choices(string.ascii_lowercase, k=m))

        return s, p

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                 min      mean     max
==========================================
find_anagrams  4.4e-06  2.8e-03  6.9e-03
==========================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Sliding Window'
    file_name = 'find-all-anagrams-in-a-string-438.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
