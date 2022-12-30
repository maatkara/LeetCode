from collections import defaultdict

import pytest

string_ = """
18. 4Sum
https://leetcode.com/problems/4sum/
Medium

Given an array nums of n integers, 
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
--------------
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
--------------
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
--------------
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

Submissions 1.9M
Acceptance Rate 36.3%
28.12.22
"""
N_MAX = int(2e2)
N_MIN = 1

A_MIN = -int(1e9)
A_MAX = int(1e9)


def four_sum(nums: list, target: int) -> list:  # submitted
    ans = []
    n = len(nums)
    if n < 4:
        return []

    avg = target // 4
    nums.sort()
    if avg < nums[0] or nums[-1] < avg:
        return []

    h = defaultdict(list)

    for i in range(n - 1):

        for j in range(i + 1, n):
            cur = nums[i] + nums[j]
            added = target - cur
            flag = 0

            if added in h:

                for pair in h[added]:
                    inds = tuple(sorted({i, j, *pair}))
                    num_l = [nums[k] for k in inds]

                    if len(inds) == 4 and num_l not in ans:
                        ans.append(num_l)

            for pair in h[cur]:
                if len({i, j, *pair}) != 4:
                    flag += 1
                    break
            if not flag:
                h[cur].append((i, j))

    return ans


def four_sum2(nums: list, target: int) -> list:  # submitted
    ans = []
    n = len(nums)
    if n < 4:
        return []

    avg = target // 4
    nums.sort()
    if avg < nums[0] or nums[-1] < avg:
        return []

    h = defaultdict(list)

    for i in range(n - 1):

        for j in range(i + 1, n):
            cur = nums[i] + nums[j]
            added = target - cur
            flag = 0

            if added in h:

                for pair in h[added]:
                    inds = tuple(sorted({i, j, *pair}))
                    num_l = tuple(nums[k] for k in inds)

                    if len(inds) == 4:
                        ans.append(num_l)

            for pair in h[cur]:
                if len({i, j, *pair}) != 4:
                    flag += 1
                    break
            if not flag:
                h[cur].append((i, j))

    return list(set(ans))


def four_sum1(nums: list, target: int) -> list:
    ans = []
    n = len(nums)
    if n < 4:
        return []
    avg = target // 4
    nums.sort()

    if avg < nums[0] or nums[-1] < avg:
        return []
    h = defaultdict(list)
    h_used = set()

    for i in range(n - 1):

        for j in range(i + 1, n):
            cur = nums[i] + nums[j]
            added = target - cur
            flag = 0

            if added in h:

                for pair in h[added]:
                    inds = tuple(sorted({i, j, *pair}))
                    num_t = tuple(nums[k] for k in inds)

                    if len(inds) == 4 and num_t not in h_used:
                        h_used.add(num_t)
                        ans.append(list(num_t))

            for pair in h[cur]:
                if len({i, j, *pair}) != 4:
                    flag += 1
                    break
            if not flag:
                h[cur].append((i, j))

    return ans


test_data = [
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([1], 0, []),

    ([-1] * 4 + [1] * 4 + [0] * 4, 0, [[-1, 0, 1, 0], [-1, -1, 1, 1], [0, 0, 0, 0]]),
    ([0, 2, 2, 3, 0, 1, 2, 3, -1, -4, 2], 0, [[-4, -1, 2, 3], [-1, 0, 0, 1], [-4, 0, 1, 3], [-4, 0, 2, 2]]),
    (list(range(A_MIN, A_MIN + N_MAX + 1)), 0, []),
    (list(range(0, N_MAX + 1)), A_MAX, []),
    (list(range(A_MAX - N_MAX, A_MAX + 1)), A_MAX, []),
]

f_l = [four_sum, four_sum1, four_sum2]


@pytest.mark.parametrize('nums, target, expected', test_data)
def test(nums, target, expected):
    for i, f in enumerate(f_l):
        ans = f(nums, target)
        print('\n', f.__name__, ans)

        assert len(ans) == len(expected)

        for an, ex in zip(sorted(ans), sorted(expected)):
            assert sorted(an) == sorted(ex)
        # assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int, n_max: int = N_MAX, a_max: int = A_MAX, n_min: int = N_MIN, a_min: int = A_MIN) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        target = randint(a_min, a_max)

        return [randint(a_min, a_max) for _ in range(n)], target

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 2e2
TIME:
             min      mean     max
======================================
four_sum   8.3e-07  4.0e-03  2.1e-02  sub
four_sum1  3.5e-07  4.0e-03  2.5e-02
four_sum2  3.3e-07  4.3e-03  2.2e-02
======================================

O(n^2) ~ 1e-5
O(n^3) ~ 1e-3
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = '4sum-18.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
