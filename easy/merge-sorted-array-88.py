import pytest

string_ = """
88. Merge Sorted Array
Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
Example 1:
----------------------
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
----------------------
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
----------------------
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:
----------------------
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9

27.07.23
"""
N_MIN = 0
N_MAX = 200
A_MAX = int(1e9)
A_MIN = -A_MAX


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    while n:
        if m and nums1[m - 1] >= nums2[n - 1]:
            nums1[n + m - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[n + m - 1] = nums2[n - 1]
            n -= 1


test_data = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1, 2, 0, 0, 0], 2, [2, 5, 6], 3, [1, 2, 2, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([1, 0], 1, [1], 1, [1, 1]),
    ([0], 0, [1], 1, [1])
]

f_l = [merge]


@pytest.mark.parametrize('nums1,m,nums2, n, expected', test_data)
def test(nums1: list[int], m: int, nums2: list[int], n: int, expected: list[int]):
    for f in f_l:
        f(nums1, m, nums2, n)
        print('\n', f.__name__, nums1)

        assert nums1 == expected


def test_time(n_iter: int = 100):
    from random import randint

    from utils.print_time4random import print_time
    # import numpy as np

    def get_args(i: int) -> tuple:
        m: int = N_MAX // 2 if i == n_iter - 1 else randint(N_MIN, N_MAX)
        n: int = N_MAX - m if i == n_iter - 1 else randint(N_MIN, N_MAX - m)
        # nums = np.random.randint(A_MIN, A_MAX+1, size=(n - m), dtype=np.longlong).tolist() + [0] * m
        if not n + m:
            m = 1

        nums1 = list(range(m)) + [0] * n
        nums2 = list(range(n))

        return nums1, m, nums2, n

    print_time(f_l, get_args, n_iter)


"""
TIME: 
==================================
merge  1.5e-07  2.3e-05  9.5e-05
==================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'merge-sorted-array-88.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
