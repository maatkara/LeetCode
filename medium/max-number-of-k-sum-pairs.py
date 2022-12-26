from collections import Counter, defaultdict

import numpy as np
import pytest

string_ = """
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/
Medium

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
------------------
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
------------------
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:
------------------
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
26.12.22
"""
N_MAX = int(1e5)
N_MIN = 1

A_MIN = 1
A_MAX = int(1e9)


def max_operations(nums: list, k: int) -> int:  # submitted
    h = defaultdict(int)
    ans = 0

    for cur in nums:
        if cur >= k:
            continue

        if h[k - cur] > 0:
            h[k - cur] -= 1
            ans += 1
        else:
            h[cur] += 1
    return ans


def max_operations1(nums: list, k: int) -> int:
    ans = 0
    h = Counter(nums)

    for cur in h:
        ans += min(h[cur], h[k - cur])

    return ans // 2


test_data = [
    ([1, 2, 3, 4], 5, 2),
    ([3, 1, 3, 4, 3], 6, 1),
    ([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3, 4),
    ([2, 5, 4, 2, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 1, 4, 2], 3, 5),

    ([3, 1, 3, 4, 3, 3, 2], 6, 3),
    ([1] * (N_MAX - 2) + [2, 2], 4, 1),
    ([1] * N_MAX, 2, N_MAX // 2),
    (list(np.random.randint(A_MIN + 2, A_MAX, N_MAX - 2)) + [1, 2], 3, 1),
]

f_l = [max_operations, max_operations1]


@pytest.mark.parametrize('nums, k, expected', test_data)
def test(nums, k, expected):
    for i, f in enumerate(f_l):
        ans = f(nums, k)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIN, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                   min      mean     max
============================================
max_operations   2.9e-03  3.2e-03  3.5e-03  sub
max_operations1  1.3e-02  1.4e-02  1.7e-02
============================================

O(n) = 1e-9 * N_MAX = 1e-4
O(n^2) = 1e-9 * N_MAX**2 = 1e1
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = "max-number-of-k-sum-pairs.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
