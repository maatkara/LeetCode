from heapq import heapify, heappush, heappop

import pytest

from utils.make_string import get_readme

string_ = """
1383. Maximum Performance of a Team
https://leetcode.com/problems/maximum-performance-of-a-team/
Hard

You are given two integers n and k and two integer arrays speed and efficiency both of length n.
There are n engineers numbered from 1 to n. 
speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied
by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 10^9 + 7.

 
Example 1:
------------
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and 
engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
------------
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 
to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
------------
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:
------------
1 <= k <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8

11.9.22
"""
N_MAX = int(1e5)
S_MAX = int(1e5)
E_MAX = int(1e8)


def max_performance(n: int, speed: list, efficiency: list, k: int) -> int:
    def key_funk(se):
        return se[0]

    P = int(1e9) + 7
    ans = 0
    sum_speed = 0
    h = []
    heapify(h)

    devops = [(eff, spd) for spd, eff in zip(speed, efficiency)]
    devops.sort(key=key_funk, reverse=True)

    for eff, spd in devops:
        heappush(h, spd)
        sum_speed += spd

        if len(h) > k:  # We need to remove one from team
            sum_speed -= heappop(h)  # Remove devops with min speed

        ans = max(ans, sum_speed * eff)

    return ans % P


test_data = [
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
    (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
]
f_l = [max_performance]


@pytest.mark.parametrize('n, speed, efficiency, k, expected', test_data)
def test(n, speed, efficiency, k, expected):
    for i, f in enumerate(f_l):
        ans = f(n, speed, efficiency, k)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    import random
    import time

    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        k = N_MAX if i == n_iter - 1 else random.randint(1, n)
        speed = [random.randint(1, S_MAX) for _ in range(n)]
        efficiency = [random.randint(1, S_MAX) for _ in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(n, speed, efficiency, k)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.12633756200011703


# -------------------------------


# TO README
def test_readme():
    topic = 'Heap'
    file_name = 'maximum_performance_of_a_team_1383.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
