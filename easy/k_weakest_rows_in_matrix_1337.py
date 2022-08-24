import heapq
import random
import time

import pytest

"""
1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Easy

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 

Constraints:
--------------
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

24.08.22
"""

N_MAX = 100
T_MAX = 0.1


def binary_search4sum(d: list, x: int, n: int) -> tuple:
    """ Бинарный поиск правый. Возвращает левый l и правый r индексы d:
    Инвариант: d[l] <= x < d[r]
    d - отсортирован по возрастанию (неубыванию)
    """
    l, r = 0, n - 1
    d = list(reversed(d))

    while r - l > 1:  # т.е не соседние
        mid = (l + r) // 2

        if d[mid] <= x:
            l = mid
        else:
            r = mid
    return n - r


def k_weakest_rows(mat: list, k) -> list:
    """Return the indices of the k weakest rows in the matrix ordered from weakest to strongest"""

    h = [(sum(j), i) for i, j in enumerate(mat)]
    del mat
    heapq.heapify(h)

    return [heapq.heappop(h)[1] for _ in range(k)]


def k_weakest_rows1(mat: list, k) -> list:
    """Return the indices of the k weakest rows in the matrix ordered from weakest to strongest"""

    h = []

    heapq.heapify(h)
    for i, row in enumerate(mat):

        sum_row = 0
        for elem in row:

            if elem:
                sum_row += 1
            else:
                continue
        h += [(sum_row, i)]
    heapq.heapify(h)
    del mat
    return [heapq.heappop(h)[1] for _ in range(k)]


def k_weakest_rows_bs(mat: list, k) -> list:
    """Return the indices of the k weakest rows in the matrix ordered from weakest to strongest"""

    n = len(mat[0])
    h = []
    for i, row in enumerate(mat):
        h += [(binary_search4sum(row, 0, n), i)]
    del mat
    heapq.heapify(h)

    return [heapq.heappop(h)[1] for _ in range(k)]


test_data = [
    ([[1, 1, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
    ([[1, 0, 0, 0],
      [1, 1, 1, 1],
      [1, 0, 0, 0],
      [1, 0, 0, 0]], 2, [0, 2]),
    ([[1, 0, 0, 0],
      [1, 1, 1, 1]], 2, [0, 1]),
    ([[1, 0, 0, 0],
      [1, 0, 0, 0]], 2, [0, 1]),
    ([[1, 1, 0, 0],
      [1, 0, 0, 0]], 2, [1, 0])
]


@pytest.mark.parametrize('mat, k, expected', test_data)
def test(mat, k, expected):
    for f in [k_weakest_rows, k_weakest_rows1, k_weakest_rows_bs]:
        assert f(mat, k) == expected


def test_time(n_iter: int = 100):
    acc = [0, 0, 0]
    f = k_weakest_rows
    f1 = k_weakest_rows1
    f2 = k_weakest_rows_bs

    for i in range(n_iter):
        m = random.randint(2, N_MAX)
        n = random.randint(2, N_MAX)
        k = random.randint(1, m)
        mat = [sorted([random.randint(0, 1) for _ in range(n)]) for _ in range(m)]

        for i, f in enumerate([f, f1, f2]):
            t0 = time.perf_counter()
            f(mat, k)
            t1 = time.perf_counter()
            acc[i] = max(acc[i], t1 - t0)

    print('\n  ', f.__name__, acc[0])  # 8.232999971369281e-05
    print('\n  ', f1.__name__, acc[1])  # 0.00018554199778009206
    print('\n  ', f2.__name__, acc[2])  # 0.00014874900080030784
