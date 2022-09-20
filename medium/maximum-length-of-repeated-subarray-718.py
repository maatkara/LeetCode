import pytest

string_ = """
718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Medium

Given two integer arrays nums1 and nums2,
return the maximum length of a subarray that appears in both arrays.
 

Example 1:
-----------------------
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
-----------------------
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 

Constraints:
-----------------------
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

20.9.22
"""
N_MAX = int(1e3)
N_MIX = 1
A_MAX = int(1e2)
A_MIN = 0


def find_length(nums1: list, nums2: list) -> int:
    """ Time O(mn), Space O(mn)"""
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
    return max(max(row) for row in dp)


def find_length_space(nums1: list, nums2: list) -> int:
    """ Time O(mn), Space O(n) - submitted to LC"""
    m, n = len(nums1), len(nums2)
    ans = 0
    prev = [0] * (n + 1)

    for i in range(m-1, -1, -1):

        cur = [0] * (n + 1)
        for j in range(n-1, -1, -1):
            if nums1[i] == nums2[j]:
                cur[j] = prev[j + 1] + 1

        ans = max(ans, max(cur))
        prev = cur

    return ans


test_data = [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
    ([59] * (N_MAX - 1), [59] * (N_MAX - 1) + [94], N_MAX - 1)
]

f_l = [find_length_space, find_length]


@pytest.mark.parametrize('nums1, nums2, expected', test_data)
def test(nums1, nums2, expected):
    for i, f in enumerate(f_l):
        ans = f(nums1, nums2)
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
==============================================
find_length_space  4.1e-02  4.2e-02  4.4e-02
find_length        4.3e-02  4.4e-02  4.7e-02
"""
# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Dp'
    file_name = 'maximum-length-of-repeated-subarray-718.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
