import pytest

string_ = """
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
-----------
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
-----------
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
-----------
1 <= n <= 45

Time complexity: O(n)
Space complexity: O(n) climb_stairs, O(1) climb_stairs_space

09.01.23
"""
N_MAX = 45
N_MIN = 1


def climb_stairs(n: int) -> int:  # fib(n+1)
    assert n > 0, f'n must be positive, got {n}'

    d = [1, 1] + [-1] * (n - 1)  # [1, 1], but fib [0, 1]

    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


def climb_stairs_space(n: int) -> int:
    prev, cur = 1, 1

    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return cur


test_data = [
    (2, 2),
    (3, 3),
    (1, 1),
    (5, 8)
]

f_l = [climb_stairs, climb_stairs_space]


@pytest.mark.parametrize('n, expected', test_data)
def test(n: int, expected: int):
    for f in f_l:
        ans = f(n)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        return n,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                 min      mean     max
==========================================
climb_stairs   4.6e-07  2.5e-06  5.3e-06
climb_stairs_space  3.7e-07  1.1e-06  2.0e-06
==========================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Dp'
    file_name = 'climbing-stairs-70.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
