import time
from collections import defaultdict
import pytest
import random
import string

"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.

"""

N_MAX = int(1e5)
T_MAX = 1


def first_unique_ch(s: str) -> int:
    """Return index of First Unique Character in a String"""

    ch_d = defaultdict(list)

    for i, ch in enumerate(s):
        ch_d[ch] += [i]

    for key, v_l in ch_d.items():
        if len(v_l) == 1:
            return v_l[0]

    return -1


test_data = [
    ("loveleetcode", 2),
    ("leetcode", 0),
    ("aabb", -1),
    ('tn'*6, -1),
    ('tn'*6 + 'a', 12)
]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    assert first_unique_ch(s) == expected


def test_time(n_iter=100):
    f = first_unique_ch
    acc = 0
    for _ in range(n_iter):
        s = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)])
        t0 = time.perf_counter()
        f(s)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)
    print('\n', acc)

    assert acc < T_MAX
