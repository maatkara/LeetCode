import random
import string

import pytest

string_ = """
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
------------------
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
------------------
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
------------------
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:
------------------
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

4.08.23
"""

N_MAX = int(1e4)
N_MIN = 1


def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])


test_data = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ('   a ', 'a')

]

f_l = [reverse_words]


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
        s = random.choices(string.ascii_letters + string.digits, k=n) + [' '] * n
        random.shuffle(s)

        return ''.join(s),

    print_time(f_l, get_args, n_iter)


"""
                 min      mean     max
==========================================
reverse_words  6.7e-07  1.3e-04  3.2e-04
==========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'reverse-words-in-a-string-151.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
