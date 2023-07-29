import random

import pytest

string_ = """
45. Jump Game II
https://leetcode.com/problems/jump-game-ii
Medium

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].

 

Example 1:
----------------------
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
----------------------
Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:
----------------------
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].


29.07.23
"""
N_MIN = 1
N_MAX = int(1e4)
A_MAX = int(1e3)
A_MIN = 0


def jump(nums: list[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            ans += 1
            break
        if i == end:  # Visited all the items on the current level
            ans += 1  # Increment the level
            end = farthest  # Make the queue size for the next level

    return ans


test_data = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2)
]

f_l = [jump]  #


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, nums)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
        min      mean     max
=================================
jump  1.0e-06  9.2e-04  2.3e-03
=================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'jump-game-ii-45.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
