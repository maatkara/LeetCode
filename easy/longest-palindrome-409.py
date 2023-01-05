import string
from collections import Counter
from random import choices

import pytest

string_ = """
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
Easy

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
-------------------
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
-------------------
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
Constraints:
-------------------
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.


Time complexity: O(n), n = len(s)
Space complexity: O(1):  the space for our count, as the alphabet size of s is fixed

04.01.23
"""
N_MAX = int(1e5)
N_MIN = 1


def longest_palindrome(s: str) -> int:
    len_p = 0
    n_odd = 0

    for v in Counter(s).values():
        even, odd = divmod(v, 2)
        len_p += even * 2
        n_odd += odd

    return len_p + 1 if n_odd else len_p


test_data = [
    ("abccccdd", 7),
    ("Abccccdd", 7),
    ("ABccccdd", 7),
    ("ABccdcCdd", 5),
    ("a", 1),
    ('aA', 1)
]

f_l = [longest_palindrome]


@pytest.mark.parametrize('s, expected', test_data)
def test(s: str, expected: int) -> bool:
    for i, f in enumerate(f_l):
        ans = f(s)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int,
                 n_max: int = N_MAX,
                 n_min: int = N_MIN,
                 ) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        s = ''.join(choices(string.ascii_letters, k=n))

        return s,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                      min      mean     max
===============================================
longest_palindrome  5.1e-06  1.9e-03  5.9e-03
===============================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Greedy'
    file_name = "longest-palindrome-409" + ".py"

    print('\n')
    print(get_readme(string_, topic, file_name))
