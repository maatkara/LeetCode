import random

import pytest

string_ = """
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Easy

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

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
----------------
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
----------------
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
----------------
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

27.07.23
"""
N_MIN = 1
N_MAX = int(3e4)
A_MAX = 100
A_MIN = -100


def remove_duplicates(nums: list[int]) -> int:
    ind = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[ind - 1]:
            nums[ind] = nums[i]
            ind += 1
    return ind


def remove_duplicates1(nums: list[int]) -> int:
    ind = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[ind - 1] and i != ind:
            nums[ind] = nums[i]
        if nums[i] != nums[ind - 1]:
            ind += 1
    return ind


test_data = [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ([1], 1)
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
remove_duplicates   2.8e-05  8.1e-04  1.7e-03
remove_duplicates1  4.4e-05  1.7e-03  3.6e-03
===============================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'remove-duplicates-from-sorted-array-26.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
