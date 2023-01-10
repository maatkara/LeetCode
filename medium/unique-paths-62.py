import pytest

string_ = """
62. Unique Paths
https://leetcode.com/problems/unique-paths/
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
-----------------
Input: m = 3, n = 7
Output: 28

Example 2:
-----------------
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
-----------------
1 <= m, n <= 100

Time complexity: O(n^2)
Space complexity: O(n)  unique_paths_space, O(n^2)  unique_paths, 

10.01.23
"""
N_MAX = int(1e2)
N_MIN = 1


def unique_paths(m: int, n: int) -> int:
    """ TC: O(n^2), SC:  O(n^2)"""
    dp = [[1] + [-1] * (n - 1) for _ in range(m)]
    dp[0] = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def unique_paths_space(m: int, n: int) -> int:
    """ Memory efficient: TC: O(n^2), SC:  O(n)"""
    prev = [1] * n

    for _ in range(1, m):

        cur = [1]

        for j in range(1, n):
            cur.append(cur[-1] + prev[j])

        prev = cur

    return prev[-1]


test_data = [
    (3, 7, 28),
    (3, 2, 3),
    (1, 1, 1),
    (1, 2, 1),
    (1, 7, 1),
    (2, 1, 1),
]

f_l = [unique_paths, unique_paths_space]


@pytest.mark.parametrize('m, n, expected', test_data)
def test(m: int, n: int, expected: int):
    for f in f_l:
        ans = f(m, n)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        m = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)

        return m, n

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                      min      mean     max
===============================================
unique_paths        1.4e-06  3.1e-04  1.2e-03
unique_paths_space  5.0e-07  2.0e-04  7.8e-04
===============================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Dp'
    file_name = 'unique-paths-62.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
