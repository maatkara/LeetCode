import pytest

string_ = """
15. 3Sum
https://leetcode.com/problems/3sum/
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
----------------------
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
----------------------
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
----------------------
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
----------------------
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Acceptance Rate 32.4%

Solution:
---------------
2 hash sets | O(n^2)
Dec 27, 2022

Intuition
 - Use num[i] as target in task two sum.
 - For each num[i] in the loop through the remaining elements of the array, use 2 sets to store elements that

    - inappropriate (h),
    - used (h_used).
    
Complexity
Time complexity: O(n^2)
Space complexity: O(n)

27.12.22
"""
N_MAX = int(3e3)
N_MIN = 3

A_MIN = -int(1e5)
A_MAX = int(1e5)


def three_sum(nums: list) -> list:
    ans = []
    i = 0
    prev = None
    nums.sort()

    for num in nums:
        if num == prev:
            i += 1
            continue

        h = set()
        h_used = set()

        for j in range(i + 1, len(nums)):
            cur = nums[j]
            added = - num - cur

            if added in h and added not in h_used:
                h_used.add(added)
                ans.append([num, added, cur])
            else:
                h.add(cur)

        prev = num
        i += 1
    return ans


test_data = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([0] * 10, [[0, 0, 0]]),
    ([1, 2] * 10, []),
    ([1, 2, 3] * 10, []),
    ([-1, -2, 3] * 10, [[-1, -2, 3]]),
    ([-1] * 4 + [1] * 4 + [0] * 3, [[-1, 0, 1], [0, 0, 0]]),
    ([0, 2, 2, 3, 0, 1, 2, 3, -1, -4, 2], [[-4, 1, 3], [-4, 2, 2], [-1, 0, 1]]),
    (list(range(A_MIN, A_MIN + N_MAX + 1)), []),
    (list(range(0, N_MAX + 1)), [])
]

f_l = [three_sum]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums, expected):
    for i, f in enumerate(f_l):
        ans = f(nums)
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

        return [randint(a_min, a_max) for _ in range(n)],

    print_time(f_l, get_args, n_iter)


"""
TIME:
             min      mean     max
======================================
three_sum  1.2e-05  1.8e-01  5.4e-01
======================================

O(n^2) = 1e-9 * N_MAX**2 = 1e-2 
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = '3sum-15.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
