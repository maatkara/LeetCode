import pytest

string_ = """
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
----------------
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
----------------
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
----------------
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

22.01.23
"""
N_MAX = int(1e5)
N_MIN = 2

A_MAX = 30
A_MIN = -30


def product_except_self(nums: list[int]) -> list[int]:  # sub
    """ TC O(n) SC = O(1) - w/o ans """
    ans = [1]

    for i in range(1, len(nums)):
        ans.append(ans[-1] * nums[i - 1])

    cur = 1
    for i in range(len(nums) - 2, -1, -1):
        cur *= nums[i + 1]
        ans[i] *= cur

    return ans


def product_except_self0(nums: list[int]) -> list[int]:
    """ TC O(n) SC = O(n) """
    ans = [1]

    for i in range(1, len(nums)):
        ans.append(ans[-1] * nums[i - 1])

    cur = [1] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
        cur[i] = cur[i + 1] * nums[i + 1]
        ans[i] *= cur[i]

    return ans


test_data = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1, 2], [2, 1]),
    ([1, 2, 1], [2, 1, 2]),
    ([0] * 10, [0] * 10)

]

f_l = [product_except_self0, product_except_self]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: bool):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        nums = np.random.randint(A_MIN, A_MAX + 1, size=n, dtype=int).tolist()

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                        min      mean     max
=================================================
product_except_self0  6.3e-04  1.2e-02  2.3e-02
product_except_self   5.4e-04  9.3e-03  1.7e-02
=================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'

    file_name = 'product-of-array-except-self-238.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
