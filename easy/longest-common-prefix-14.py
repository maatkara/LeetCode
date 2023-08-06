import random
import string

import pytest

string_ = """
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

6.08.23
"""

N_MAX = 200
N_MIN = 1


def longest_common_prefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    prev = strs[0]
    pref = ''

    for cur in strs[1:]:
        if not cur or not prev or cur[0] != prev[0]:
            return ''
        pref = prev[0]
        for chp, chc in zip(prev[1:], cur[1:]):
            if chp != chc:
                prev = pref
                break
            pref += chp
            prev = pref

    return pref


def longest_common_prefix2(strs: list[str]) -> str:  # submitted
    if len(strs) == 1:
        return strs[0]

    pref = strs[0]

    for cur in strs[1:]:
        if not cur or not pref or cur[0] != pref[0]:
            return ''
        i = 1
        for chp, chc in zip(pref[1:], cur[1:]):
            if chp != chc:
                break
            i += 1
        pref = pref[:i]

    return pref


def longest_common_prefix3(strs: list[str]) -> str:  # submitted
    if len(strs) == 1:
        return strs[0]

    strs.sort()
    pref, cur = strs[0],  strs[-1]

    if not cur or not pref or cur[0] != pref[0]:
        return ''
    i = 1
    for chp, chc in zip(pref[1:], cur[1:]):
        if chp != chc:
            break
        i += 1
    pref = pref[:i]

    return pref


def longest_common_prefix1(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    i = min([len(s) for s in strs])
    if not i:
        return ''

    pref = strs[0][:i]

    for cur in strs[1:]:
        if not cur or cur[0] != pref[0]:
            return ''

        for j, (chp, chc) in enumerate(zip(pref[:i], cur[:i])):
            if chp != chc:
                i = j
                break

    return pref[:i]


test_data = [
    (["flower", "flow", "flight"], 'fl'),
    (["flower", "", "flight"], ''),
    (["dog", "racecar", "car"], ''),
    (["dog", "dom", "delaverr", "delaverr"], 'd'),
    (["dom", "dom", "delaverr"], 'd'),
    (["dog", "dom", "dolaverr"], 'do'),
    ([''], ''),
    (['', "dom"], ''),
    (['dog'], 'dog')

]

f_l = [longest_common_prefix, longest_common_prefix1, longest_common_prefix2, longest_common_prefix3]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    for f in f_l:
        ans = f(s)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        s = []
        for j in range(n):
            m = random.randint(0, N_MAX)
            s.append(''.join(random.choices(string.ascii_lowercase, k=m)))

        random.shuffle(s)

        return s,

    print_time(f_l, get_args, n_iter)


"""
                          min      mean     max
===================================================
longest_common_prefix   4.9e-07  1.6e-06  8.6e-06
longest_common_prefix1  1.0e-06  8.6e-06  2.8e-05
longest_common_prefix2  3.3e-07  8.3e-07  4.1e-06  sub
longest_common_prefix3  4.7e-07  1.1e-05  2.9e-05
===================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'longest-common-prefix-14.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
