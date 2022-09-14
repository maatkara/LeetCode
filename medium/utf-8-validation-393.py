import pytest

from utils.make_string import get_readme

string_ = """
393. UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/
Medium

Given an integer array data representing the data, return whether it is a valid UTF-8 encoding
(i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, 
followed by n - 1 bytes with the most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: 
The input is an array of integers.
Only the least significant 8 bits of each integer is used to store the data. 
This means each integer represents only 1 byte of data.


Example 1:
--------------------------
Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:
--------------------------
Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
 

Constraints:
--------------------------
1 <= data.length <= 2 * 10^4
0 <= data[i] <= 255

13.9.22
"""
N_MAX = int(2e4)
A_MAX = 255


def valid_utf_8(data: list) -> bool:
    """ Return whether it is a valid UTF-8 encoding

    :param data: list[int] an integer array representing the data

                128         192        224        240        248
    borders  | 10000000 | 11000000 | 11100000 | 11110000 | 11111000 -  the octet sequence
    bytes   1|    -     |         2|         3|         4|        5
             for next n-1 bytes
    """
    n = len(data)
    m = 5
    borders = [0] * m

    for i in range(1, 6):
        s = '1' * i + '0' * (8 - i)
        borders[i - 1] = int(s, 2)

    i = 0

    while i < n:

        j = 0  # Find number of bytes
        while j < m and borders[j] <= data[i]:  # First number
            j += 1

        if j == 1:  # j == 1: not for first - code only for next n-1 bytes
            return False
        if not j:
            j += 1
        if j == m or i + j > n:  # Number of  bytes > 4 | len(data) < number of  bytes
            return False

        while j > 1:  # next n-1 bytes
            i += 1
            if borders[0] <= data[i] < borders[1]:  # [128 : 192) <==> ['1000000','11000000')
                j -= 1
            else:
                return False
        i += 1
    return True


test_data = [
    ([197, 130, 1], True),
    ([197, 130], True),
    ([235, 140, 4], False),
    ([251, 6, 8], False),
    ([240, 162, 138, 147], True),
    ([240, 162, 138], False),
    ([1], True),
    ([127], True)

]
f_l = [valid_utf_8]


@pytest.mark.parametrize('data, expected', test_data)
def test(data: list, expected):
    for i, f in enumerate(f_l):
        ans = f(data)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    import random
    import time

    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        data = [random.randint(0, A_MAX) for _ in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(data)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 5.366e-06


# -------------------------------


# TO README
def test_readme():
    topic = 'Bit manipulation'
    file_name = 'utf-8-validation-393.py'
    print('\n')
    print(get_readme(string_, topic, file_name))