import time

import pytest
import random

"""
13. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

N_MAX = 15
simbols_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s_big_l = ['V', 'X', 'L', 'C', 'D', 'M']
s_small_l = ['I', 'X', 'C']
prev_d = {prev: s_small_l[i // 2] for i, prev in enumerate(s_big_l)}


def roman2integer(s: str) -> int:
    prev = ''
    integer = 0

    for ch in reversed(s):
        condition = -1 * ((prev in prev_d and ch == prev_d[prev]) * 2 - 1)
        integer += simbols_d[ch] * condition
        prev = ch

    return integer


test_data = [
    ("MCMXCIV", 1994),
    ("LVIII", 58),
    ("III", 3),
    ("I", 1),
]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    assert roman2integer(s) == expected


def test_time(n_iter=100):
    f = roman2integer
    acc = 0
    for _ in range(n_iter):
        s = ''.join([random.choice(list(simbols_d.keys())) for _ in range(1, N_MAX + 1)])
        t0 = time.perf_counter()
        f(s)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)
    print('\n', acc)

    assert acc < 15e-6
