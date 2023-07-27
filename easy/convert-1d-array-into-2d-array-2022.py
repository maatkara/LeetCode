import pytest

string_ = """
2022. Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
Easy

You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. 
You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, 
the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.


Example 1:
--------------------
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

Example 2:
--------------------
Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

Example 3:
--------------------
Input: original = [1,2], m = 1, n = 1
Output: []
Explanation: There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
 

Constraints:
--------------------
1 <= original.length <= 5 * 10^4
1 <= original[i] <= 10^5
1 <= m, n <= 4 * 10^4

27.07.23
"""
N_MIN = 1
N_MAX = int(5e4)
A_MAX = int(1e4)
A_MIN = 1


def construct_2d_array(original: list[int], m: int, n: int) -> list[list[int]]:
    return [[original[i * n + j] for j in range(n)]
            for i in range(m)] if m * n == len(original) else []


test_data = [
    ([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),
    ([1, 2, 3], 1, 3, [[1, 2, 3]]),
    ([1, 2], 1, 1, []),
    ([1],  1, 1, [[1]])
]

f_l = [construct_2d_array]


@pytest.mark.parametrize('original, m, n, expected', test_data)
def test(original: list[int], m: int, n: int, expected: int):
    for f in f_l:
        ans = f(original, m, n)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from random import randint

    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        nums = np.random.randint(A_MIN, A_MAX, n, dtype=int).tolist()
        nn = int(0.8 * n) if i == n_iter - 1 else randint(1, n)
        m = n // nn

        return nums, m, nn

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                      min      mean     max
===============================================
construct_2d_array  4.3e-07  8.6e-07  2.9e-06
===============================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'convert-1d-array-into-2d-array-2022.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
