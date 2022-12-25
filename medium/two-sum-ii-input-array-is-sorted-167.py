import pytest

string_ = """
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

**Your solution must use only constant extra space.**


Example 1:
--------------
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
--------------
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
--------------
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:
--------------
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

Acceptance Rate 60.0%
25.12.22
"""
N_MAX = int(3e4)
N_MIN = 2

A_MIN = -int(1e3)
A_MAX = int(1e3)


def two_sum1(numbers: list, target: int) -> list:  # submitted
    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[r] + numbers[l] == target:
            return [l + 1, r + 1]
        if numbers[r] + numbers[l] > target:
            r -= 1
        else:
            l += 1
    return [-1]


def two_sum(numbers: list, target: int) -> list:
    """ Two pointer"""
    n = len(numbers)

    for i in range(n - 1):
        added = target - numbers[i]
        j = i + 1

        while j < n and numbers[j] <= added:
            if numbers[j] == added:
                return [i + 1, j + 1]
            j += 1

    return [-1]


test_data = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([3, 3], 6, [1, 2]),
    ([3, 3, 4], 6, [1, 2]),

    ([2, 2, 2], 6, [-1]),
    ([2, 2, 3, 3], 6, [3, 4]),

    ([0] * 10, 2, [-1]),
    # (sorted(randint(A_MIN, A_MAX) for _ in range(N_MAX)), 2 * A_MAX, [-1]),
    # ([0] * (N_MAX - 2) + [1, 1], 2, [N_MAX - 1, N_MAX]),
    # ([A_MIN] * (N_MAX // 2 - 1) + [1, 1] + [A_MAX] * (N_MAX // 2 - 1), 2, [N_MAX // 2, N_MAX // 2 + 1]),
    # (list(range(N_MAX - 2)) + [N_MAX - 2, N_MAX - 1], 2 * N_MAX - 3, [N_MAX - 1, N_MAX]),
]

f_l = [two_sum, two_sum1]


@pytest.mark.parametrize('numbers, target, expected', test_data)
def test(numbers, target, expected):
    for i, f in enumerate(f_l):
        ans = f(numbers, target)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 10):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIN, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
            min      mean     max
=====================================
two_sum   1.1e+01  1.1e+01  1.1e+01
two_sum1  1.2e-03  1.3e-03  1.4e-03  submitted
=====================================

O(n^2) = 1e-9 * N_MAX**2 ~ 1
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'
    file_name = 'two-sum-ii-input-array-is-sorted-167.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
