import random
import string

import pytest

string_ = """
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
Easy

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.

3.08.23
"""

N_MAX = int(1e4)
N_MIN = 1


def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


test_data = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    (' g', 1),
    ('  g   ', 1)

]

f_l = [length_of_last_word]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    for f in f_l:
        ans = f(s)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX // 2 if i == n_iter - 1 else random.randint(N_MIN, N_MAX - 1)
        m = N_MAX - n  # spaces
        s = random.choices(string.ascii_lowercase, k=n) + [' '] * n
        random.shuffle(s)

        return ''.join(s),

    print_time(f_l, get_args, n_iter)


"""
                       min      mean     max
================================================
length_of_last_word  2.3e-06  8.9e-05  2.1e-04
================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'length-of-last-word-58.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
