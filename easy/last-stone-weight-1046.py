import heapq

import pytest

string_ = """
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
Easy

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
 
Example 1:
------------------
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
------------------
Input: stones = [1]
Output: 1

Constraints:
------------------
1 <= stones.length <= 30
1 <= stones[i] <= 1000

14.01.23
"""
N_MAX = 30
N_MIN = 1

A_MAX = 1000
A_MIN = 1


def last_stone_weight(stones: list[int]) -> int:
    """ Stack. TC O(n log n) SC = O(n) """
    stones = [-st for st in stones]  # for max-heap, O(n)
    heapq.heapify(stones)  # O(n)

    while stones:
        y = heapq.heappop(stones)  # O(log n)
        x = heapq.heappop(stones) if stones else 0  # O(log n)

        if not stones:
            return x - y  # x, y < 0

        if x != y:
            heapq.heappush(stones, y - x)  # < 0,  O(log n)

    return 0


test_data = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([2, 7, 4, 1, 8, 1, 1], 0),
    ([2, 7, 4, 1, 8, 1, 1, 1], 1),
    ([1, 1, 1, 1, 1, 1], 0),
    ([1, 1, 1, 1, 1], 1),
    ([1], 1),
    ([1, 2], 1),
    (list(range(A_MIN, A_MAX, 34)), 32),
    (list(range(N_MIN, N_MAX + 1)), 1)
]

f_l = [last_stone_weight]


@pytest.mark.parametrize('stones, expected', test_data)
def test(stones: list[int], expected: int):
    for f in f_l:
        ans = f(stones)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        stones = np.random.randint(A_MIN, A_MAX + 1, size=n, dtype=int).tolist()

        return stones,

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                     min      mean     max
==============================================
last_stone_weight  8.3e-07  6.7e-06  2.0e-05
==============================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Heap'

    file_name = 'last-stone-weight-1046.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
