import time
from collections import Counter
import heapq
import pytest
import random

"""
1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/
Medium

You are given an integer array arr.
You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
 

Constraints:

2 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

N_MAX = int(1e5)  # % 2 = 0
X_MAX = int(1e5)


def min_set_size(arr: list) -> int:
    """ Return the minimum size of the set so that at least half of the integers of the array are removed.
     (Heap)
      """

    n = len(arr)
    f_d = Counter(arr)
    del arr
    f_l = [-v for v in f_d.values()]
    del f_d
    heapq.heapify(f_l)

    set_size = 0
    m = 0
    while m < n / 2:
        m -= heapq.heappop(f_l)  # max = - min
        set_size += 1

    return set_size


arr_r = list(range(2, N_MAX))
test_data = [
    ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
    ([1, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4),
    ([7, 7, 7, 7, 7, 7], 1),
    (arr_r, (N_MAX - 2) / 2)
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    f = min_set_size
    assert f(arr) == expected


def test_time(n_iter=100):
    f = min_set_size
    acc = 0
    for _ in range(n_iter):
        arr = [random.randint(1, X_MAX) for _ in range(2, N_MAX)]
        t0 = time.perf_counter()
        f(arr)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)  # 0.027

    print(acc)

    # max time
    arr = list(range(2, N_MAX + 1))
    t0 = time.perf_counter()
    f(arr)
    t1 = time.perf_counter()
    acc = max(acc, t1 - t0)

    print('\n', acc)  # 0.035

    assert acc < 0.1
