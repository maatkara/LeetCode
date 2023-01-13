import string

import pytest

string_ = """
394. Decode String
https://leetcode.com/problems/decode-string/
Medium
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc.
 Furthermore, you may assume that the original data does not contain any digits and 
 that digits are only for those repeat numbers, k. 
 For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Example 1:
------------------------
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
------------------------
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
------------------------
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:
------------------------
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

13.01.23
"""
N_MAX = 30
N_MIN = 1
A_MIN = 1
A_MAX = 300


def decode_string(s: str) -> str:
    """ Stack. TC O(n) SC = O(n) """

    stack = []
    cur_n, cur_s = 0, ''

    for ch in s:
        if ch == '[':
            stack.extend([cur_s, cur_n])
            cur_n, cur_s = 0, ''

        elif ch == ']':
            n = stack.pop()
            prev_s = stack.pop()
            cur_s = prev_s + n * cur_s

        elif ch.isdigit():
            cur_n = cur_n * 10 + int(ch)
        else:
            cur_s += ch

    return cur_s


test_data = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("10[abc]3[cd]ef", 10 * "abc" + 3 * "cd" + "ef"),
    ("109[abc]3[cd]ef", 109 * "abc" + 3 * "cd" + "ef"),
    ('dfghjk', 'dfghjk'),
    ('d', 'd'),
    ('d2[3[ab]]', 'd' + 6 * 'ab'),
    ('d5[]', 'd'),
    ('d5[2[]]', 'd'),
]

f_l = [decode_string]


@pytest.mark.parametrize('s, expected', test_data)
def test(s: str, expected: str):
    for f in f_l:
        ans = f(s)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint, choices

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        k: int = N_MAX // 5 if i == n_iter - 1 else randint(0, N_MAX // 5)
        digits = [randint(A_MIN, A_MAX) for _ in range(k)]
        s = choices(string.ascii_lowercase, k=min(n, 4))
        s_all = min(n, 4)

        for dig in digits:
            if n - s_all - len(str(dig)) - 2 < 0:
                return s,
            k1 = min(randint(0, n // 5), n - s_all - len(str(dig)) - 2)
            s += f'{dig}[{choices(string.ascii_lowercase, k=k1)}]'
            s_all = len(s)
        return s,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                 min      mean     max
==========================================
decode_string  3.2e-07  2.1e-06  6.5e-06
==========================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Stack'

    file_name = 'decode-string-394.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
