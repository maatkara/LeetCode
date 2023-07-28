import random

import pytest

string_ = """
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Medium
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. More formally, 
if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
 

Example 1:
--------------------
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, 
with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
--------------------
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, 
with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
--------------------
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

28.07.23
"""
N_MIN = 1
N_MAX = int(3e4)
A_MAX = int(1e4)
A_MIN = -A_MAX


def remove_duplicates1(nums: list[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    ind = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[ind - 1] or nums[i] != nums[ind - 2]:
            nums[ind] = nums[i]
            ind += 1
    return ind


def remove_duplicates(nums: list[int]) -> int:  # sub
    if len(nums) < 3:
        return len(nums)

    ind = 2
    for num in nums[2:]:
        if num != nums[ind - 1] or num != nums[ind - 2]:
            nums[ind] = num
            ind += 1
    return ind


test_data = [
    ([1, 1, 1, 2, 2, 3], 5),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
    ([1, 1, 2], 3),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 9),
    ([1], 1),
    ([-1, 1], 2)
]

f_l = [remove_duplicates, remove_duplicates1]  #


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums.copy())
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        nums: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()
        nums.sort()

        return nums,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                      min      mean     max
===============================================
remove_duplicates   4.1e-05  1.6e-03  3.7e-03
remove_duplicates1  4.8e-05  2.0e-03  5.4e-03
===============================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'remove-duplicates-from-sorted-array-ii-80.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
