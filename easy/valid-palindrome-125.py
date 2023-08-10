import random
import re
import string

import pytest

string_ = """
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

10.08.23
"""

N_MAX = int(2e5)
N_MIN = 1


def is_palindrome(s: str) -> bool:
    s = re.sub(r"[^a-z0-9]", '', s.lower())

    if len(s) < 2:
        return True
    i = 0
    j = len(s) - 1

    while i <= len(s) // 2:  # ?
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


test_data = [
    ("A man, a plan, #a canal: Panama", True),
    ("A man, a plan, a canal: Panama", True),
    ("A man, a plan, a fcanal: Panama", False),
    ("race a car", False),
    ("ab_a", True),
    (' ', True),
    (".,", True)
]

f_l = [is_palindrome]


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

        s = ''.join(random.choices(string.ascii_letters + string.digits + ' .,:&%$#@!', k=n))

        return s,

    print_time(f_l, get_args, n_iter)


""" 
                 min      mean     max
==========================================
is_palindrome  6.5e-05  2.9e-03  7.8e-03
==========================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'
    file_name = 'valid-palindrome-125.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
