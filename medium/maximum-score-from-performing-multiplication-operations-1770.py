import pytest

string_ = """
1770. Maximum Score from Performing Multiplication Operations
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
Medium

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m.
The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

Example 1:
--------------------------------
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
--------------------------------
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 
At first glance, the solution seems to be greedy, 
but if you try to greedily take the largest value from the beginning or the end, this will not be optimal.
You should try all scenarios but this will be costy.
Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity, 
and hence dp is a perfect choice here.

Constraints:
--------------------------------
n == nums.length
m == multipliers.length
1 <= m <= 10^3
m <= n <= 10^5
-1000 <= nums[i], multipliers[i] <= 1000

16.9.22
"""
N_MAX = int(1e5)
M_MAX = int(1e3)
A_MAX = int(1e3)  # +-


def maximum_score(nums: list, multipliers: list) -> int:
    """ Space Optimized Dynamic Programming. Time: O(m^2), Space: O(m)"""
    n = len(nums)
    m = len(multipliers)

    prev = [0] * (m + 1)  # Starting with the last operation i=m-1 => next operation (i.e. prev) can't be done => 0

    for i in range(m - 1, -1, -1):

        cur = [0] * (i + 1)
        for l in range(i, -1, -1):
            r = n - 1 - (i - l)
            cur[l] = max(
                prev[l + 1] + nums[l] * multipliers[i],
                prev[l] + nums[r] * multipliers[i]
            )
        prev = cur

    return prev[0]


test_data = [
    ([1, 2, 3], [3, 2, 1], 14),
    ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102)
]

f_l = [maximum_score]


@pytest.mark.parametrize('nums, multipliers, expected', test_data)
def test(nums: list, multipliers, expected):
    for i, f in enumerate(f_l):
        ans = f(nums, multipliers)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 10):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=1, a_min=-A_MAX, n_iter=n_iter)


"""
TIME:
                 min      mean     max
==========================================
maximum_score  4.5e+00  4.6e+00  4.8e+00 
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'maximum-score-from-performing-multiplication-operations-1770.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
