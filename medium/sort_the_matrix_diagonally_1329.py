import heapq
import random
import time

import numpy as np
import pytest

"""
1329. Sort the Matrix Diagonally
https://leetcode.com/problems/sort-the-matrix-diagonally/
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and 
going in the bottom-right direction until reaching the matrix's end. 

For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix,
includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


Example 1:
-----------------------
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:
-----------------------
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

Constraints:
-----------------------
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

28.8.22
"""
N_MAX = 100
A_MAX = 100


def diagonal_sort(mat: list) -> list:
    m, n = len(mat), len(mat[0])

    if m == 1 or n == 1:
        return mat

    def sort_matrix_rc(is_col=False):
        m_, n_ = (n, m) if is_col else (m, n)

        def l_ranges(i, is_col=is_col):  # function for 2 usage zip and with different is_col
            col, row = range(n_), range(i, m_)
            return zip(col, row) if is_col else zip(row, col)

        for i in range(is_col, m_ - 1):
            d = [mat[ii][jj] for ii, jj in l_ranges(i)]  # diagonal, m-1: last element -> not change, it only one
            heapq.heapify(d)

            for ii, jj in l_ranges(i):
                mat[ii][jj] = heapq.heappop(d)

    sort_matrix_rc()
    sort_matrix_rc(is_col=True)

    return mat


test_data = [
    ([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]], [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]),
    ([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4],
      [84, 28, 14, 11, 5, 50]],
     [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66],
      [84, 28, 75, 33, 55, 68]]),
    ([[10, 7, 8, 9, 5, 3]], [[10, 7, 8, 9, 5, 3]]),
    ([[10], [7], [8], [9], [5], [3]], [[10], [7], [8], [9], [5], [3]]),
    ([[1]], [[1]])

]
f_l = [diagonal_sort]


@pytest.mark.parametrize('mat, expected', test_data)
def test(mat, expected):
    for f in f_l:
        print('\n', f.__name__)
        assert f(mat) == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        m = random.randint(1, N_MAX)
        n = random.randint(1, N_MAX)

        if i==n_iter-1:
            m = n = N_MAX
        mat = np.random.randint(1, A_MAX, size=(m, n)).tolist()

        for i, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(mat)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)
    for i, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[i])  # 0.0027922550034418236

