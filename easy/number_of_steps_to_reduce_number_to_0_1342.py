import random
import time

import pytest

"""
1342. Number of Steps to Reduce a Number to Zero
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Easy

Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:

Input: num = 123
Output: 12
 

Constraints:
0 <= num <= 10^6

25.08.22
"""

N_MAX = int(1e6)


def number_of_steps_naive(num: int) -> int:
    k = 0
    while num:
        if not num % 2:
            num /= 2
        else:
            num -= 1
        k += 1

    return k


def number_of_steps1(num: int) -> int:
    k = 1
    while num > 1:
        k += 1 + num % 2
        num //= 2
    return k if num else 0


def number_of_steps_bin(num: int) -> int:
    s = bin(num)
    return len(s) - 2 + s.count('1') - 1  # -2 <= 123='0b1111011', -1 - left first 1


test_data = [
    (14, 6),
    (8, 4),
    (14, 6),
    (15, 7),
    (123, 12),
    (122, 11),
    (2, 2),
    (0, 0),
    (2 ** 20, 21)
]


@pytest.mark.parametrize('num, expected', test_data)
def test(num, expected):
    for f in [number_of_steps_bin, number_of_steps_naive, number_of_steps1]:  #
        print('\n', f.__name__)
        assert f(num) == expected


def test_time(n_iter: int = 100):
    f_l = [number_of_steps_naive, number_of_steps1, number_of_steps_bin]
    acc = [0] * len(f_l)
    for _ in range(n_iter):
        n = random.randint(0, N_MAX)

        for i, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(n)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)

    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])


"""
number_of_steps_naive 5.30299985257443e-06
number_of_steps1      2.310000127181411e-06
number_of_steps_bin   1.5890000213403255e-06
"""
