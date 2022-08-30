import random
import time

import numpy as np
import pytest

from utils.make_string import get_readme

string_ = """
48. Rotate Image
https://leetcode.com/problems/rotate-image/
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.


Example 1:
-------------------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
-------------------
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
-------------------
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

30.8.22
"""

N_MAX = 20
A_MAX = 1000


def rotate(matrix: list) -> None:
    """ Do not return anything, modify matrix in-place instead. """
    n = len(matrix)

    if n == 1:
        return

    matrix.reverse()

    for i in range(n):
        for j in range(i, n):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return


test_data = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),

    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),

]

f_l = [rotate]


@pytest.mark.parametrize('mat, expected', test_data)
def test(mat, expected):
    for f in f_l:
        print('\n', f.__name__)
        f(mat)
        print(f.__name__, mat)
        assert mat == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX - 5)
        matrix = np.array(np.random.randint(-A_MAX, A_MAX, (n, n), dtype=int)).tolist()

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(matrix)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 3.2e-05


# -------------------------------
# TO README
def test_readme():
    topic = 'Array'
    file_name = 'rotate_image_48.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Array | [Python](https://github.com/maatkara/LeetCode/blob/main/medium/rotate_image_48.py) | Medium|
"""
