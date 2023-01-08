import sys

import numpy as np
import pytest

string_ = """
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
-------------------
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
-------------------
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
-------------------
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Time complexity: O(h), h - tree height, worst = O(n)
Space complexity: O(n) - recursive

08.01.23
"""
N_MAX = 100  # 300 PyCharm rise segmentation error 139
N_MIN = 1

A_MAX = 1
A_MIN = 0
"""
  ([[1, 1, 1],
    [0, 1, 0],
    [1, 1, 1]], 1),
    
"""
sys.setrecursionlimit(10000)


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    num = 0
    seen = set()

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1' or (i, j) in seen:
            return

        seen.add((i, j))
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i, j) not in seen:
                dfs(i, j)
                num += 1
    return num


test_data = [
    ([["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]], 1),
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]], 3),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "1", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "1", "1", "1"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "1", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "1", "1", "1", "1"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "1", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["1", "1", "1", "1", "1"]], 1),

    ([["1", "1", "1"],
      ["0", "1", "0"],
      ["1", "1", "1"]], 1),

    ([['1']], 1),
    ([['0']], 0),
    ([['0'] * 3 for _ in range(5)], 0),
    ([['1'] * 3 for _ in range(5)], 1),
    ([['1'] * 3 for _ in range(5)], 1),

    ([['1', '0', '1']], 2),
    (np.array(np.eye(N_MAX, dtype=int), dtype=str).tolist(), N_MAX),
    (np.ones((5, 3), dtype=str).tolist(), 1),
    (np.zeros((N_MAX, N_MAX - 5), dtype=str).tolist(), 0),
    (np.ones((N_MAX, N_MAX - 5), dtype=str).tolist(), 1),

]

f_l = [num_islands]


@pytest.mark.parametrize('greed, expected', test_data)
def test(greed: list[list[str]], expected: int):
    for f in f_l:
        ans = f(greed)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        m = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        if i == n_iter - 1:
            greed = np.ones((m, n))
        else:
            greed = np.random.randint(A_MIN, A_MAX + 1, size=(m, n))

        return greed.astype('str').tolist(),

    print_time(f_l, get_args, n_iter)


"""
TIME: 
A_MAX = 100  PyCharm rise segmentation error 139 
             in case of recursion limit > 10k
               min      mean     max
========================================
num_islands  2.0e-05  1.6e-03  1.7e-02
========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Graph, DFS'
    file_name = 'number_of_islands_200.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
