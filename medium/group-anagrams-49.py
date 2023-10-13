import random
import string
from collections import defaultdict

import pytest

string_ = """
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

13.10.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e2)
A_MIN = 0


def group_anagrams(strs: list[str]) -> list[list[str]]:  # submitted
    strs_table = defaultdict(list)

    for s in strs:
        strs_table[''.join(sorted(s))].append(s)

    return list(strs_table.values())


test_data = [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    (["bat", "eat", "tea", "tan", "ate", "nat"], [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]),
    ([""], [[""]]),
    (["a"], [["a"]])

]

f_l = [group_anagrams]


@pytest.mark.parametrize('t, expected', test_data)
def test(t: list[str], expected: list[list[str]]):
    for f in f_l:
        ans = f(t)
        print('\n', f.__name__, ans)

        assert ans == expected  # all(an in expected for an in ans) and all(an in ans for an in expected)


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m: int = A_MAX if i == n_iter - 1 else random.randint(A_MIN, A_MAX)

        arr = [""] * n

        for i in range(n):
            arr[i] = ''.join(random.choices(string.ascii_lowercase, k=m))
        return arr,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                   min      mean     max
============================================
group_anagrams1  6.7e-05  2.3e-02  8.2e-02
============================================
 
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'group-anagrams-49.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
