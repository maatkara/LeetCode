import pytest

string_ = """
985. Sum of Even Numbers After Queries
https://leetcode.com/problems/sum-of-even-numbers-after-queries/
Medium

You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
--------------
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Example 2:
--------------
Input: nums = [1], queries = [[4,0]]
Output: [0]

Constraints:
--------------
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
1 <= queries.length <= 10^4
-10^4 <= vali <= 10^4
0 <= indexi < nums.length

21.9.22 !!!
"""
N_MAX = int(1e4)
N_MIX = 1
A_MAX = int(1e4)
A_MIN = -int(1e4)


def sum_even_after_queries(nums: list, queries: list) -> list:
    ans = [0] * len(queries)
    s = sum(num for num in nums if not num % 2)

    for i, (v_add, j) in enumerate(queries):
        old, nums[j] = nums[j], nums[j] + v_add
        s += nums[j] * (~nums[j] % 2) - old * (~old % 2)
        ans[i] = s

    return ans


def sum_even_after_queries_bit(nums: list, queries: list) -> list:
    ans = [0] * len(queries)
    s = sum(num for num in nums if not num & 1)

    for i, (v_add, j) in enumerate(queries):
        old, nums[j] = nums[j], nums[j] + v_add
        s += nums[j] * (~nums[j] & 1) - old * (~old & 1)
        ans[i] = s

    return ans


test_data = [
    ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
    ([1], [[4, 0]], [0]),
    ([0, 2, 2, 2], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [6, 4, 4, 6])
]

f_l = [sum_even_after_queries, sum_even_after_queries_bit]


@pytest.mark.parametrize('nums, queries, expected', test_data)
def test(nums, queries, expected):
    for i, f in enumerate(f_l):
        ans = f(nums.copy(), queries)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIX, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                              min      mean     max
=======================================================
sum_even_after_queries      2.8e-04  3.0e-04  3.3e-04
sum_even_after_queries_bit  3.4e-04  3.6e-04  3.9e-04

"""

# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'sum-of-even-numbers-after-queries-985.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
