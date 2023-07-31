import random

import pytest

string_ = """
274. H-Index
https://leetcode.com/problems/h-index/
Medium

Given an array of integers citations where citations[i] is the number of citations
 a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h 
such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:
---------------
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers 
in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the 
remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
---------------
Input: citations = [1,3,1]
Output: 1
 

Constraints:
---------------
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

31.07.23
"""
N_MIN = 1
N_MAX = int(5e3)
A_MAX = int(1e3)
A_MIN = 0


def h_index(citations: list[int]) -> int:
    citations.sort(reverse=True)
    for i, cit in enumerate(citations):
        if i >= cit - 1:
            return max(cit, i)

    return len(citations)


test_data = [
    ([3, 0, 6, 1, 5], 3),
    ([8, 0, 6, 1, 5], 3),
    ([3, 1, 1, 1, 1], 1),
    ([4, 4, 0, 0], 2),
    ([3, 3, 0, 0], 2),
    ([2, 2, 2, 2, 0], 2),
    ([1, 3, 1], 1),
    ([3], 1),
    ([1], 1),
    ([0], 0),
    ([4, 4, 4, 4, 4, 4, 5], 4),
    ([0] * 5 + [5], 1)
]

f_l = [h_index]  #


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list[int], expected: list[int]):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

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
====================================
h_index  1.4e-05  3.1e-04  7.5e-04
====================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'h-index-274.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
