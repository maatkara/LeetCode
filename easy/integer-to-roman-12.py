import random

import pytest

string_ = """
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
 which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999

03.08.23
"""

N_MAX = 3999
N_MIN = 1

simbols_d: dict[int, str] = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
s_small_l = ['I', 'X', 'C', 'M']
five_l = ['V', 'L', 'D', '']


def integer2roman(num: int) -> str:
    s = ''
    r = 0

    while num:
        num, i = divmod(num, 10)

        if not i:
            r += 1
            continue

        if i * 10 ** r in simbols_d:
            s = simbols_d[i * 10 ** r] + s
        elif i in (4, 9):
            s = s_small_l[r] + simbols_d[(i + 1) * 10 ** r] + s
        else:
            s = five_l[r] * (i > 5) + s_small_l[r] * (i - (i > 5) * 5) + s

        # print(i, r, s, num)
        r += 1

    return s


test_data = [
    (1994, "MCMXCIV"),
    (58, "LVIII"),
    (3, "III"),
    (1, "I"),
    (3325, 'MMMCCCXXV'),
    (40, 'XL'),
    (1000, 'M'),
    (25, 'XXV'),
    (3999, 'MMMCMXCIX')
]

f_l = [integer2roman]


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

        return n,

    print_time(f_l, get_args, n_iter)


"""
                 min      mean     max
==========================================
integer2roman  1.0e-06  2.1e-06  4.5e-06
==========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'roman_to_integer_13.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
