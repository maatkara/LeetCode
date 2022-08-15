import sys

from math import inf
import pytest
import random
import time

"""
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

см также
https://stepik.org/lesson/41234/step/5

Найти максимум в каждом окне размера m данного массива чисел A[1 . . . n].

Вход. Массив чисел A[1 . . . n] и число 1 ≤ m ≤ n.
Выход. Максимум подмассива A[i . . . i + m − 1] для всех 1 ≤ i ≤ n − m + 1.
Задача — реализовать алгоритм со временем работы O(n)

Формат входа. Первая строка входа содержит число n,
вторая — массив A[1 . . . n], третья — число m.

Формат выхода. n − m + 1 максимумов, разделённых пробелами.

Ограничения. 1 ≤ n ≤ 10 5 , 1 ≤ m ≤ n, 0 ≤ A[i] ≤ 10^5 для всех 1 ≤ i ≤ n.

Sample Input 1:
3
2 1 5
1

Sample Output 1:
2 1 5

Sample Input 2:
8
2 7 3 1 5 2 6 2
4

Sample Output 2:
7 7 5 6 6


Ограничения.
------------------
1  ≤ n ≤ int(1e5)
1 ≤ m ≤ n.
10^4 ≤ A[i] ≤ 10^3
T_MAX = 3
256 Mb


"""

N_MAX = int(4e5)
A_MAX = int(1e4)
T_MAX = 3


class StackMax:
    """ Max support stack (LIFO)"""

    def __init__(self):
        self.stack_max = []

    def push(self, x):
        """Add element to stack"""

        max_prev = float(-inf) if not self.stack_max else self.stack_max[-1]

        if x > max_prev:
            max_prev = x

        self.stack_max += [max_prev]

    def max(self):
        """Return max stack element"""
        return self.stack_max[-1] if self.stack_max else float(-inf)

    def pop(self):
        """  Remove stack last element """
        if self.stack_max:
            self.stack_max.pop()


class StackSlidingWindowMax:

    def __init__(self, window: int):
        self.window = window
        self.left_max = float(-inf)
        self.right = StackMax()
        self.window_l = []  # Sliding window

    def manage(self, a_l: list) -> list:
        """ Return Sliding Window Maximum """

        if self.window == 1:
            return a_l

        n = len(a_l)
        slide_w_l = [0] * (n - self.window + 1)  # to return
        i = 0  # index in slide_w_l
        k = self.fill_window(a_l, i, n)  # fill window_l = a_l[i:i+k], k=min(window, n)
        self.fill_right()  # right size = window or len(rest of a_l)

        while k < n:

            k = self.fill_window(a_l, k, n)  # -> k = i + window

            for x in self.window_l:
                slide_w_l[i] = self.max()
                self.right.pop()
                if x > self.left_max:
                    self.left_max = x
                i += 1

            self.shift()

        # Last circle: max from right (we have only right, left is clear )
        while i < n - self.window + 1:
            slide_w_l[i] = self.right.max()
            self.right.pop()
            i += 1

        return slide_w_l

    def max(self) -> int:
        """ Return max(left_max, right.max)"""

        if self.left_max >= self.right.max():
            return self.left_max
        return self.right.max()

    def shift(self):
        """  Moves the entire "left stack" to right with maximum recalculation"""

        self.fill_right()
        self.left_max = float(-inf)

    def fill_right(self):
        """ Fill right stack with maximum recalculation """
        for x in reversed(self.window_l):
            self.right.push(x)

    def fill_window(self, a_l: list, i: int, n: int) -> int:
        """ Fill window_l = a_l[i:i+k], k=min(window, n) """

        k = i + self.window if i + self.window < n else n
        self.window_l = [a_l[j] for j in range(i, k)]

        return k


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    n = next(reader)[0]
    a_l = next(reader)
    m = next(reader)[0]

    assert (n > 1) and m <= n

    stack = StackSlidingWindowMax(m)
    answer_l = stack.manage(a_l, n)

    if answer_l:
        print(*answer_l)


test_data = [
    ([2, 1, 5], 1, [2, 1, 5]),
    ([2, 1, 5], 3, [5]),
    ([2, 7, 3, 1, 5, 2, 6, 2], 4, [7, 7, 5, 6, 6]),
    ([2, 3, 9], 3, [9]),
    ([73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16], 7, [73, 97, 97, 97, 97, 97, 97, 97, 42]),
    ([73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16], 15, [97]),
    ([5] * 125, 125, [5]),
    ([28, 7, 64, 40, 68, 86, 80, 93, 4, 53, 32, 56, 68, 18, 59], 12, [93, 93, 93, 93]),
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 3, [9, 8, 7, 6, 5, 4, 3, 2]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4, [9, 8, 7, 6, 5, 4, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 5, [9, 8, 7, 6, 5, 4]),
    ([1, 4, 5, 6, 1, 1, 1, 1], 4, [6, 6, 6, 6, 1]),
    ([1, 1, 1, 1, 10], 2, [1, 1, 1, 10]),
    ([1, 0, 2, 2, 2, 2, 0, 0], 4, [2, 2, 2, 2, 2]),
    ([-5769, -7887, -5709, 4600, -7919, 9807, 1303, -2644, 1144, -6410, -7159, -2041, 9059, -663, 4612, -257, 2870,
      -6646, 8161, 3380, 6823, 1871, -4030, -1758, 4834, -5317, 6218, -4105, 6869, 8595, 8718, -4141, -3893, -4259,
      -3440, -5426, 9766, -5396, -7824, -3941, 4600, -1485, -1486, -4530, -1636, -2088, -5295, -5383, 5786, -9489,
      3180, -4575, -7043, -2153, 1123, 1750, -1347, -4299, -4401, -7772, 5872, 6144, -4953, -9934, 8507, 951, -8828,
      -5942, -3499, -174, 7629, 5877, 3338, 8899, 4223, -8068, 3775, 7954, 8740, 4567, 6280, -7687, -4811, -8094, 2209,
      -4476, -8328, 2385, -2156, 7028, -3864, 7272, -1199, -1397, 1581, -9635, 9087, -6262, -3061, -6083, -2825, -8574,
      5534, 4006, -2691, 6699, 7558, -453, 3492, 3416, 2218, 7537, 8854, -3321, -5489, -945, 1302, -7176, -9201, -9588,
      -140, 1369, 3322, -7320, -8426, -8446, -2475, 8243, -3324, 8993, 8315, 2863, -7580, -7949, 4400],
     6,
     [9807, 9807, 9807, 9807, 9807, 9807, 1303, 9059, 9059, 9059, 9059, 9059, 9059, 8161, 8161, 8161, 8161, 8161, 8161,
      6823, 6823, 6218, 6218, 6869, 8595, 8718, 8718, 8718, 8718, 8718, 8718, 9766, 9766, 9766, 9766, 9766, 9766, 4600,
      4600, 4600, 4600, -1485, -1486, 5786, 5786, 5786, 5786, 5786, 5786, 3180, 3180, 1750, 1750, 1750, 1750, 5872,
      6144, 6144, 6144, 8507, 8507, 8507, 8507, 8507, 8507, 7629, 7629, 7629, 8899, 8899, 8899, 8899, 8899, 8899, 8740,
      8740, 8740, 8740, 8740, 6280, 6280, 2209, 2385, 2385, 7028, 7028, 7272, 7272, 7272, 7272, 7272, 9087, 9087, 9087,
      9087, 9087, 9087, 5534, 5534, 5534, 6699, 7558, 7558, 7558, 7558, 7558, 7558, 8854, 8854, 8854, 8854, 8854, 8854,
      1302, 1302, 1302, 1369, 3322, 3322, 3322, 3322, 3322, 8243, 8243, 8993, 8993, 8993, 8993, 8993, 8993]
     ),
    ([-5769, -7887, -5709, 4600, -7919, 9807, 1303, -2644, 1144, -6410, -7159, -2041, 9059, -663, 4612, -257, 2870,
      -6646, 8161, 3380, 6823, 1871, -4030, -1758, 4834, -5317, 6218, -4105, 6869, 8595, 8718, -4141, -3893, -4259,
      -3440, -5426, 9766, -5396, -7824, -3941, 4600, -1485, -1486, -4530, -1636, -2088, -5295, -5383, 5786, -9489, 3180,
      -4575, -7043, -2153, 1123, 1750, -1347, -4299, -4401, -7772, 5872, 6144, -4953, -9934, 8507, 951, -8828, -5942,
      -3499, -174, 7629, 5877, 3338, 8899, 4223, -8068, 3775, 7954, 8740, 4567, 6280, -7687, -4811, -8094, 2209, -4476,
      -8328, 2385, -2156, 7028, -3864, 7272, -1199, -1397, 1581, -9635, 9087, -6262, -3061, -6083, -2825, -8574, 5534,
      4006, -2691, 6699, 7558, -453, 3492, 3416, 2218, 7537, 8854, -3321, -5489, -945, 1302, -7176, -9201, -9588, -140,
      1369, 3322, -7320, -8426, -8446, -2475, 8243, -3324, 8993, 8315, 2863, -7580, -7949, 4400],
     6,
     [9807, 9807, 9807, 9807, 9807, 9807, 1303, 9059, 9059, 9059, 9059, 9059, 9059, 8161, 8161, 8161, 8161, 8161, 8161,
      6823, 6823, 6218, 6218, 6869, 8595, 8718, 8718, 8718, 8718, 8718, 8718, 9766, 9766, 9766, 9766, 9766, 9766, 4600,
      4600, 4600, 4600, -1485, -1486, 5786, 5786, 5786, 5786, 5786, 5786, 3180, 3180, 1750, 1750, 1750, 1750, 5872,
      6144, 6144, 6144, 8507, 8507, 8507, 8507, 8507, 8507, 7629, 7629, 7629, 8899, 8899, 8899, 8899, 8899, 8899, 8740,
      8740, 8740, 8740, 8740, 6280, 6280, 2209, 2385, 2385, 7028, 7028, 7272, 7272, 7272, 7272, 7272, 9087, 9087, 9087,
      9087, 9087, 9087, 5534, 5534, 5534, 6699, 7558, 7558, 7558, 7558, 7558, 7558, 8854, 8854, 8854, 8854, 8854, 8854,
      1302, 1302, 1302, 1369, 3322, 3322, 3322, 3322, 3322, 8243, 8243, 8993, 8993, 8993, 8993, 8993, 8993])
]


@pytest.mark.parametrize('a_l,  window, expected', test_data)
def test(a_l, window, expected):
    stack = StackSlidingWindowMax(window)
    assert stack.manage(a_l) == expected


def test_time(n_iter: int = 10):
    acc = 0
    n = N_MAX

    for i in range(n_iter):
        a_l = [random.randint(-A_MAX, A_MAX) for _ in range(n)]
        m = random.randint(1, n)

        t0 = time.perf_counter()
        stack = StackSlidingWindowMax(m)
        stack.manage(a_l)
        t1 = time.perf_counter()
        acc = max(acc, t1 - t0)
    print('\n  ', acc)

    m = 2
    a_l = [random.randint(-A_MAX, A_MAX) for _ in range(n)]
    t0 = time.perf_counter()
    stack = StackSlidingWindowMax(m)
    stack.manage(a_l)
    t1 = time.perf_counter()

    acc = max(acc, t1 - t0)
    print(acc)

    assert acc <= T_MAX


if __name__ == '__main__':
    main()
