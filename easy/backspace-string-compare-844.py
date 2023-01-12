import itertools
import random
import string

import pytest

string_ = """
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/?envType=study-plan&id=level-1
Easy

Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
----------------
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
----------------
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
----------------
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
----------------
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

12.01.23
"""
N_MAX = int(2e2)
N_MIN = 1


def backspace_compare_old(s: str, t: str) -> bool:
    """ TC: O(n), SC:  O(1)"""

    i, j = len(s) - 1, len(t) - 1
    skip_s = skip_t = 0

    while i >= 0 and j >= 0:
        if s[i] == '#' or t[j] == '#':
            skip_s += (s[i] == '#')
            skip_t += (s[i] == '#')
        elif skip_s or skip_t:
            skip_s -= 1 * skip_s
            skip_t -= 1 * skip_t
        elif s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            return False

    return i == j


def backspace_compare_stack(s: str, t: str) -> bool:
    """ Stack. TC O(n+m) SC = O(n+m) """

    def get_string(chs):
        stack = []

        for ch in chs:
            if ch == '#' and stack:
                stack.pop()
            else:
                stack.append(ch)
        return stack

    s = get_string(s)
    t = get_string(t)

    if len(s) != len(t):
        return False

    for ch1, ch2 in zip(s, t):
        if ch1 != ch2:
            return False

    return True


def backspace_compare_gen(s: str, t: str) -> bool:  # sub
    """ Generator. TC O(n), SC = O(1) """

    def gen_string(chs):
        skip = 0

        for ch in chs[::-1]:
            if ch == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield ch

    for ch1, ch2 in itertools.zip_longest(gen_string(s), gen_string(t), fillvalue='-'):
        if ch1 != ch2:
            return False

    return True


test_data = [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("ab#cd#", "c#d", False),
    ("ab#cdd#", "acc#d", True),
    ("a#c", "b", False),
]

f_l = [backspace_compare_stack, backspace_compare_gen]


@pytest.mark.parametrize('secret, guess, expected', test_data)
def test(secret: str, guess: str, expected: bool):
    for f in f_l:
        ans = f(secret, guess)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint, choices

    def get_args(i: int) -> tuple:
        n1: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        n2: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        k1: int = N_MAX // 10 if i == n_iter - 1 else randint(0, N_MAX // 10)
        k2: int = N_MAX // 10 if i == n_iter - 1 else randint(0, N_MAX // 10)

        if i == n_iter - 1:
            s = ['a'] * (n1 - k1) + ['#'] * k1
            t = ['a'] * (n2 - k2) + ['#'] * k2
        else:
            s = choices(string.ascii_lowercase, k=n1 - k1) + ['#'] * k1
            t = choices([str(i) for i in range(10)], k=n2 - k2) + ['#'] * k2
        random.shuffle(s)
        random.shuffle(t)
        return ''.join(s), ''.join(t)

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                           min      mean     max
====================================================
backspace_compare_stack  2.7e-06  1.2e-05  2.6e-05
backspace_compare_gen    1.1e-06  1.7e-06  2.3e-05  sub
====================================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Stack, Two pointer'

    file_name = 'backspace-string-compare-844.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
