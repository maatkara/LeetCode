import time
import pytest
import random
from collections import deque

"""
659. Split Array into Consecutive Subsequences
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

You are given an integer array nums that is sorted in non-decreasing order.

Determine 
if it is possible to split nums into one or more subsequences such that both of the following conditions are true:
 - Each subsequence is a consecutive increasing sequence
          (i.e. each integer is exactly one more than the previous integer).
 - All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array
by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements.
(i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:
---------------
Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5

Example 2:
---------------
Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5

Example 3:
---------------
Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

Constraints:[1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
---------------
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
"""

N_MAX = int(1e5)
X_MAX = int(1e3)
X_MIN = -int(1e3)


def is_possible(nums: list) -> bool:
    """ Determine if it is possible to split nums into one or more subsequences such that
        both of the following conditions are true:
             - Each subsequence is a consecutive increasing sequence
              (i.e. each integer is exactly one more than the previous integer).
             - All subsequences have a length of 3 or more.
    Return true if you can split nums according to the above conditions, or false otherwise.

    :param nums: an integer array that is sorted in non-decreasing order

    Идея: массив частот в каждый "момент" есть количество одновременно растущих ПП

    Поскольку подпоследовательности (ПП) фактически range(min, max+1), т.е. строго возрастающие на +1 на каждом элементе
        0) находим min max and length for nums (x_min, x_max, n)
        1) создадим массив d частот для всех чисел от x_min до x_max. Размер d d_size = n+2. d[0]=0.
        2) фактически, d[i] - количество ПП, которые "продолжают расти",
         поскольку одинаковые числа м.б. только в разных ПП.
         Будем "убирать" ПП, которые перестали расти и "закончили" набор чисел.
        3) Создадим массив rank=deque(). Будем хранить размер ПП.
        4) В цикле по d:
            изменение delta = d[i] - d[i-1] - изменение кол-ва ПП:
            delta > 0: кол-во ПП увеличилось на delta -> push - добавим в массив rank delta элементов(те ПП) размером 1,
                    длина остальных ПП увеличились на 1
            delta < 0: кол-во ПП уменьшилось на delta -> pop - убираем из массива rank delta элементов(те ПП),
                    длина остальных ПП увеличились на 1
                    m = pop - длина удаляемой ПП. Если m < 3 -> return False

            delta == 0: кол-во ПП не изменилось, длина всех ПП увеличились на 1

        В массива rank проверяем длину оставшихся в конце ПП:
        return max(rank) > 2

    Example:
    -----------
    nums =   [1,  2,  3,   4,    4,  5]

    integers: 1   2   3    4     5
    d =   [0, 1,  1,  1,   2,    1]
    delta     1   0   0    1    -1
    rank =   [1] [2] [3] [4, 1] [2]

    Return False because rank (that is subsequence length) at the end < 3 (2 < 3)

    Pseudocode:
    -----------
    Найти min max, первый элемент и length for nums (x_min, x_max, num0, n)
    Создать и заполнить массив частот d размером d_size = max_x - min_x +2
              d[0] = 0,
              d[i] - частота числа  в nums для i >= 1: i=num-num0+1. d[i]=0 в случае, если число отсутствует в nums.
    Создать двустороннюю очередь rank
    Для i в интервале от 1 до d_size-1:
        delta <- d[i] - d[i - 1]

        if delta > 0:
            rank.extend([0] * delta)  # Add delta new elements to the rank
        elif delta < 0:
            for h in range(-delta):
                m <- rank.popleft()
                if m < 3:
                    return False
        Обновить очередь rank прибавив 1 к каждому значению

    return min(rank) > 2
    ----------------------------

    In English:

    Idea | Explanations | Example | Pseudocode | Python solution
    ----------------
    Idea: the array of frequencies at each "moment" is the **number of simultaneously growing subsequences** (SS)

    Explanations
    Since subsequences are strictly increasing by +1 at each element
    0) find min, max, first element and length for nums (x_min, x_max, num0, n)
    1) build d - array of frequencies for all numbers from x_min to x_max. Size d = x_max - x_min + 2. d[0]=0.
    2) in fact, d[i] is the number of subsequences that "keep growing",
         since the same numbers can be only in different SSs.
         We will "remove" the subsequences that have stopped growing and have "finished" gaining numbers.
    3) Build an array rank=deque(). We will store the size of the subsequences.
    4) Looping over d:
            change delta = d[i] - d[i-1] - change in the number of subsequences:
            delta > 0: the number of SSs has increased by delta ->
                    push - add elements (i.e. SSs) of size 1 to the array rank,
                    the length of the remaining SS increased by 1
            delta < 0: the number of SSs decreased by delta ->
                    pop - remove elements from the array rank (those SSs),
                    the length of the remaining SSs increased by 1
                    m = pop - the length of the removed SSs. If m < 3 -> return False

            delta == 0: the number of SSs has not changed, the length of all SSs has increased by 1

    return min(rank) > 2

    Example:
    -----------
    nums =   [1,  2,  3,   4,    4,  5]

    integers: 1   2   3    4     5
    d =   [0, 1,  1,  1,   2,    1]
    delta     1   0   0    1    -1
    rank =   [1] [2] [3] [4, 1] [2]

    Return False because rank (that is subsequence length) at the end < 3 (2 < 3)

    ~Pseudocode:
    -----------
    Find min, max, first element and length for nums (x_min, x_max, num0, n)
    Create an array d of size = max_x - min_x + 2 and fill it with 0
    For num in nums: fill array d with frequencies num. d[0]=0.
    Create a deque rank
    for i in range from 1 to d_size-1:
        delta <- d[i] - d[i - 1]
        if delta > 0:
            rank.extend([0] * delta)  # Add delta new elements to the rank
        elif delta < 0:
            for h in range(-delta):
                m <- rank.popleft()
                if m < 3:
                    return False
        Update the queue rank by adding 1 to each value
    return min(rank) > 2
    """

    n = 0
    x_max = -float('inf')
    x_min = float('inf')
    len_min = 3

    for num in nums:  # O(n)
        n += 1
        if num > x_max:
            x_max = num
        if num < x_min:
            x_min = num

    if n < len_min:
        return False
    d_size = (x_max - x_min + 2)
    d = [0] * d_size  # d[i]: nums.count(num) *for num in nums
    num0 = nums[0]

    # Bild d
    for i, num in enumerate(nums):  # O(n)
        d[num - num0 + 1] += 1
    del nums

    # d
    rank = deque()
    for i in range(1, d_size):
        delta = d[i] - d[i - 1]

        if delta > 0:
            rank.extend([0] * delta)  # Add delta new elements to the rank

        elif delta < 0:
            for h in range(-delta):
                m = rank.popleft()
                if m < len_min:
                    return False

        rank = deque([x + 1 for x in rank])  # Update deque

    # Check for length < len_min
    return min(rank) > 2


test_data = [
    ([1], False),
    ([1] * 18, False),
    ([1] * 17 + [3], False),
    ([1, 2, 3, 4, 6, 7, 8, 9, 10, 11], True),  #
    ([1, 2, 3, 3, 4, 5], True),
    ([1, 2, 3, 3, 4, 4, 5, 5], True),
    ([1, 2, 3, 4, 4, 5], False),
    ([1, 2, 3, 5, 5, 6, 7], False),  #
    (list(range(30)), True),
    (list(range(-30, -1, 1)) + list(range(2, 30)), True),
    (sorted(list(range(20)) * 3), True),
    (list(range(-X_MAX, 0, 1)) + list(range(2, X_MAX)), True),
    (list(range(-30, 1, 1)) + list(range(30)), True),
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    f = is_possible
    assert f(arr) == expected


def test_time(n_iter=100):
    f = is_possible
    acc = 0

    for _ in range(n_iter):
        arr = sorted([random.randint(X_MIN, X_MAX) for _ in range(N_MAX)])
        t0 = time.perf_counter()
        f(arr)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)  # ~0.026
    print('\n', acc)

    assert acc < 0.1
