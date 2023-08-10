import random
import string

import pytest

string_ = """
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

10.08.23
"""

N_MAX = int(1e3)
N_MIN = 1


def convert(s: str, numRows: int) -> str:
    n = len(s)
    if n == 1 or numRows == 1 or n <= numRows:
        return s

    n_zigzag = 2 * numRows - 2
    c, r = divmod(n, n_zigzag)
    c *= (1 + numRows - 2)
    c += 1 * (r > 0) + (r - numRows) * (r > numRows)

    matrix = [[''] * c for _ in range(numRows)]
    r = c = 0

    for i in range(n):
        matrix[r][c] = s[i]

        if i % n_zigzag < numRows - 1:
            r += 1
        else:
            r -= 1
            c += 1
    # print(matrix)
    return ''.join([''.join(matrix[i]) for i in range(numRows)])


test_data = [
    ("PAYPALISHIRINGs", 3, "PAHNAPLSIIGYIRs"),
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRIN", 3, "PAHNAPLSIIYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
    ("PAYPALISHIRING", 20, "PAYPALISHIRING"),
    ("ABCDEFGHIJKLMN", 2, 'ACEGIKMBDFHJLN'),
    ('ABX', 2, 'AXB'),
    ('A', 2, 'A'),

]

f_l = [convert]


@pytest.mark.parametrize('s, s1, expected', test_data)
def test(s, s1, expected):
    for f in f_l:
        ans = f(s, s1)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m = random.randint(N_MIN, n)

        s = ''.join(random.choices(string.ascii_letters + ',.', k=n))

        return s, m

    print_time(f_l, get_args, n_iter)


""" 
          min      mean     max
====================================
convert  4.1e-07  4.2e-04  1.9e-03
====================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'zigzag-conversion-6.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
