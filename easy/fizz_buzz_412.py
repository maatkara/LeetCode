import random
import time

import pytest

"""
412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
Easy

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 10^4

24.08.22
"""

N_MAX = int(1e4)
T_MAX = 0.1


def fizz_buzz(n: int) -> list:
    """ If log(n, base=3) is an integer -> True"""

    ans_l = []
    ans_t = ((3, "Fizz"), (5, "Buzz"))

    for i in range(1, n + 1):
        
        str0 = ''
        for j, _ in ans_t:
            if not i % j:
                str0 += _
        ans_l += [str0 if str0 else str(i)]

    return ans_l


test_data = [
    (3, ["1", "2", "Fizz"]),
    (1, ["1"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

]


@pytest.mark.parametrize('n, expected', test_data)
def test(n, expected):
    f = fizz_buzz
    assert f(n) == expected


def test_time(n_iter: int = 100):
    acc = 0
    f = fizz_buzz

    for i in range(n_iter):
        n = random.randint(1, N_MAX + 1)
        t0 = time.perf_counter()
        f(n)
        t1 = time.perf_counter()
        acc = max(acc, t1 - t0)

    print('\n  ', acc)   # 0.0023

    t0 = time.perf_counter()
    f(N_MAX)
    t1 = time.perf_counter()
    acc = max(acc, t1 - t0)

    print('\n  ', acc)
    assert acc < 0.01  # 0.0023
