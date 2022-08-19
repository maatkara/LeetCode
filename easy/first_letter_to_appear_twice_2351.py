import time
from collections import defaultdict
import pytest
import random
import string

"""
2351. First Letter to Appear Twice
https://leetcode.com/problems/first-letter-to-appear-twice/

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice,
because out of all the letters the index of its second occurrence is the smallest.

Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.

"""

N_MAX = int(1e2)
T_MAX = 1


def first_2_ch(s: str) -> str:
    """Return First Letter to Appear Twice"""

    ch_d = defaultdict(int)

    for i, ch in enumerate(s):
        ch_d[ch] += 1
        if ch_d[ch] == 2:
            return ch


test_data = [
    ("abcdd", 'd'),
    ("abccbaacz", 'c'),
    ("loveleetcode", 'l'),
    ("leetcode", 'e'),
    ("aabb", 'a'),
    ('tn' * 6 + 'a', 't')
]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    assert first_2_ch(s) == expected


def test_time(n_iter=100):
    f = first_2_ch
    acc = 0
    for _ in range(n_iter):
        s = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)])
        t0 = time.perf_counter()
        f(s)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)
    print('\n', acc)

    assert acc < T_MAX
