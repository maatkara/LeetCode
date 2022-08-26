import random
import time
from collections import Counter
from itertools import permutations
from math import log2, floor

import pytest

"""
869. Reordered Power of 2
https://leetcode.com/problems/reordered-power-of-2/
Medium

You are given an integer n.
We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:
--------------
Input: n = 1
Output: true

Example 2:
--------------
Input: n = 10
Output: false
 

Constraints:
--------------
1 <= n <= 10^9
26.08.22
"""

N_MAX = int(1e9)


def reordered_power_of_2_naive(n: int) -> bool:
    """naive"""
    if n < 3:
        return True

    for w in permutations(str(n)):
        if not int(w[0]) or int(w[-1]) % 2:
            continue
        if bin(int(''.join(w)))[2:].count('1') == 1:
            return True
    return False


def reordered_power_of_2_log(n: int) -> bool:
    """naive"""

    if n < 3:
        return True

    def check_log(n):
        wlog = log2(n)
        return wlog == floor(wlog)

    if check_log(n):
        return True

    for w in permutations(str(n)):
        if not int(w[0]) or int(w[-1]) % 2:
            continue
        if check_log(int(''.join(w))):
            return True
    return False


def reordered_power_of_2(n: int) -> bool:

    if n < 3:
        return True

    s = str(n)

    n_len = len(s)
    nc = Counter(s)
    k_min = (10 ** (n_len - 1)).bit_length()
    k_max = (10 ** n_len).bit_length()

    for i in range(k_min, k_max):
        if nc == Counter(str(2 ** i)):
            return True

    return False


test_data = [
    (1, True),
    (2, True),
    (256, True),
    (652, True),
    (526, True),
    (10, False),
    (2 ** 20, True),
    (2 ** 29, True),
    (2 ** 29 + 1, False),
    (10 ** 9, False)

]

f_l = [reordered_power_of_2, reordered_power_of_2_naive, reordered_power_of_2_log]


@pytest.mark.parametrize('n, expected', test_data)
def test(n, expected):
    for f in f_l:
        print('\n', f.__name__)
        assert f(n) == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for _ in range(n_iter):
        n = random.randint(1, N_MAX // 10)

        for i, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(n)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)

    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])

    # Max time
    n = N_MAX
    for i, f in enumerate(f_l):
        t0 = time.perf_counter()
        f(n)
        t1 = time.perf_counter()
        acc[i] = max(acc[i], t1 - t0)

    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])


"""
Max time
reordered_power_of_2 2.17119995795656e-05

reordered_power_of_2_naive 0.8092218249985308

reordered_power_of_2_log 0.7510416790028103
"""
