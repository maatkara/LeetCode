import random

import pytest

string_ = """
27. Remove Element
https://leetcode.com/problems/remove-element/
Easy
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Custom Judge:
-------------------
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 
Example 1:
-------------------
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
-------------------
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
-------------------
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

27.07.23
"""
N_MIN = 0
N_MAX = 100
A_MAX = 50
A_MIN = 0


def remove_element(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val and nums[slow] == val:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != val:
            slow += 1
    return slow


test_data = [
    ([3, 2, 2, 3], 3, 2),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ([0, 1, 2, 2, 3, 0, 4, 2], 87, 8),
    ([0] * 8, 0, 0),
    ([0] * 8, 1, 8),
    ([], 5, 0)
]

f_l = [remove_element]


@pytest.mark.parametrize('nums, val, expected', test_data)
def test(nums: list[int], val: int, expected: list[int]):
    for f in f_l:
        ans = f(nums, val)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m = random.randint(N_MIN, n)
        val = random.randint(N_MIN, N_MAX)
        nums = [val] * m + np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()
        random.shuffle(nums)

        return nums, val

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                  min      mean     max
===========================================
remove_element  5.3e-07  9.3e-06  4.2e-05
===========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'remove-element-27.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
