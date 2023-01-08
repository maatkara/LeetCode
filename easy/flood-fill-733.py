import sys

import numpy as np
import pytest

string_ = """
733. Flood Fill
https://leetcode.com/problems/flood-fill/
Easy

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
---------------------------
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color 
as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
---------------------------
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:
---------------------------
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n

Time complexity: O(n)
Space complexity: O(n) - recursive

08.01.23
"""
N_MAX = 50
N_MIN = 1

A_MAX = 2 ** 16 - 1
A_MIN = 0

sys.setrecursionlimit(N_MAX ** 2 * 4)


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    seen = set()
    origin = image[sr][sc]

    if color == origin:
        return image

    m, n = len(image), len(image[0])

    assert m > 0 and n > 0, f"m & n must be positive integer, but m={m} n={n}"
    assert 0 <= sr < m and 0 <= sc < n, f"sr={sr} m={m} sc={sc} n={n}"

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen:
            return

        seen.add((i, j))
        if image[i][j] == origin:
            image[i][j] = color

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    dfs(sr, sc)
    return image


arr = np.zeros((N_MAX, N_MAX), dtype=np.int32)
arr[-1, -1] = 1
arr_exp = np.zeros((N_MAX, N_MAX), dtype=np.int32)
arr_exp[-1, -1] = 1
arr_exp[arr == 0] = 6
test_data = [
    ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[1, 1, 1], [1, 2, 0], [1, 0, 1]], 1, 1, 6, [[1, 1, 1], [1, 6, 0], [1, 0, 1]]),
    ([[1, 1, 1], [1, 2, 0], [1, 2, 1]], 1, 1, 6, [[1, 1, 1], [1, 6, 0], [1, 6, 1]]),
    ([[1, 1, 1], [1, 2, 2], [1, 0, 1]], 1, 1, 6, [[1, 1, 1], [1, 6, 6], [1, 0, 1]]),
    ([[1, 1, 1], [2, 2, 0], [1, 0, 1]], 1, 1, 6, [[1, 1, 1], [6, 6, 0], [1, 0, 1]]),
    ([[1, 2, 1], [1, 2, 0], [1, 0, 1]], 1, 1, 6, [[1, 6, 1], [1, 6, 0], [1, 0, 1]]),
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ([[0]], 0, 0, 1, [[1]]),
    (arr.tolist(), 0, 0, 6, arr_exp.tolist())
]

f_l = [flood_fill]


@pytest.mark.parametrize('image, sr, sc, color, expected', test_data)
def test(image: list[list[int]], sr: int, sc: int, color: int, expected: list[list[int]]):
    for f in f_l:
        ans = f(image, sr, sc, color)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        m = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        if i == n_iter - 1:
            image = np.zeros((m, n), dtype=np.int32)
            image[-1, -1] = 1
            sr, sc, color = 0, 0, A_MAX
        else:
            image = np.random.randint(A_MIN, A_MAX, size=(m, n))
            sr, sc, color = randint(0, m - 1), randint(0, n - 1), randint(0, A_MAX)

        return image.tolist(), sr, sc, color

    print_time(f_l, get_args, n_iter)


"""
TIME:
              min      mean     max
=======================================
flood_fill  2.3e-06  2.9e-05  2.3e-03
=======================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Graph, DFS'
    file_name = 'flood-fill-733.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
