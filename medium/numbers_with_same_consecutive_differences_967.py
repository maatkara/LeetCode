import random
import time

import pytest

from utils.make_string import get_readme

string_ = """
967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
Medium

Return all non-negative integers of length n such that
 the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.
You may return the answer in any order.


Example 1:
-------------------
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
-------------------
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:
-------------------
2 <= n <= 9
0 <= k <= 9

3.9.22
"""

N_MAX = 9


def nums_same_consec_diff_dfs(n, k) -> list:
    R_MAX = 10

    def dfs(i: int, r: int, subseq) -> int:
        nonlocal ans, k

        subseq += str(i)

        if not r:
            ans.append(int(subseq))
            return

        j_l = set([i - k] * (i - k >= 0) + [i + k] * (i + k < R_MAX))

        for j in j_l:
            dfs(j, r - 1, subseq)

    ans = []
    subseq = ''

    for i in range(1, R_MAX):
        dfs(i, n - 1, subseq)

    return ans


def nums_same_consec_diff_bfs(n: int, k: int) -> list:
    R_MAX = 10

    if n == 1:
        return [i for i in range(R_MAX)]

    queue = [digit for digit in range(1, R_MAX)]

    for level in range(n - 1):

        next_q = []

        for num in queue:
            tail = num % 10  # last digit
            next_digits = set([tail + k] * (tail + k < R_MAX) + [tail - k] * (tail - k >= 0))

            for nxt in next_digits:
                next_q += [num * 10 + nxt]

            queue = next_q

    return queue


test_data = [
    (3, 7, [181, 292, 707, 818, 929]),
    (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    (2, 9, [90]),
    (3, 9, [909]),
    (3, 0, [111, 222, 333, 444, 555, 666, 777, 888, 999])

]
f_l = [nums_same_consec_diff_dfs, nums_same_consec_diff_bfs]


@pytest.mark.parametrize('n, k, expected', test_data)
def test(n, k, expected):
    for i, f in enumerate(f_l):
        ans = f(n, k)
        print('\n', f.__name__, ans)
        assert len(ans) == len(expected)
        for ans_i in ans:
            assert ans_i in expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(2, N_MAX + 1)
        k = N_MAX if i == n_iter - 1 else random.randint(0, N_MAX + 1)

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(n, k)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for j, f in enumerate(f_l):
        print(f'\n  {f.__name__}: {acc[j]}')


"""
TIME:
  nums_same_consec_diff_dfs: 0.0016721760002837982
  nums_same_consec_diff_bfs: 0.001033432999975048
"""


# -------------------------------

# # TO README
def test_readme():
    topic = 'Tree'
    file_name = 'numbers_with_same_consecutive_differences_967' + '.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/medium/numbers_with_same_consecutive_differences_967.py) | Medium|

"""
