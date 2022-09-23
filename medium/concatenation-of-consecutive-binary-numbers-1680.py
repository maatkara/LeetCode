import sys

import pytest

string_ = """
1680. Concatenation of Consecutive Binary Numbers
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
Medium

Given an integer n, 
return the decimal value of the binary string formed by 
concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example 1:
-----------------
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example 2:
-----------------
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:
-----------------
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^9 + 7, the result is 505379714.
 
Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

Constraints:
-----------------
1 <= n <= 10^5

23.9.22
"""
N_MAX = int(1e5)
N_MIX = 1


def concatenated_binary(n: int) -> int:
    P = int(1e9) + 7
    ans = 1

    for i in range(2, n + 1):
        ans = (ans << i.bit_length()) % P + i
    return ans % P


def concatenated_binary_rec(n: int) -> int:
    P = int(1e9) + 7
    sys.setrecursionlimit(N_MAX)

    def helper(i):
        return (helper(i - 1) << i.bit_length()) % P + i if i > 1 else 1

    return helper(n) % P


test_data = [
    (1, 1),
    (3, 27),
    (12, 505379714)

]

f_l = [concatenated_binary_rec, concatenated_binary]


@pytest.mark.parametrize('n, expected', test_data)
def test(n, expected):
    for i, f in enumerate(f_l):
        ans = f(n)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX,  # a_max=A_MAX,
               n_min=N_MIX,  # a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                           min      mean     max
====================================================
concatenated_binary      3.2e-04  3.3e-04  3.8e-04
concatenated_binary_rec  1.9e-03  2.5e-03  4.2e-02

"""

# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Bit manipulation'
    file_name = 'concatenation-of-consecutive-binary-numbers-1680.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
