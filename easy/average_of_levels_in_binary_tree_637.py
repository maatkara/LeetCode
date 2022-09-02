import random
import time

import pytest

from utils.binary_tree import BinaryTree, TreeNode
from utils.make_string import get_readme

string_ = """
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Easy

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
-------------------
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
-------------------
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:
-------------------
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

2.9.22
"""

N_MAX = int(1e4)
A_MAX = 2 ** 31 - 1  # +-


def average_of_levels_dfs(root_l: list) -> list:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # -----------------------------

    if not root:
        return 0

    if not root.left and not root.right:  # is None
        return [root.val]

    def dfs(node: TreeNode, i: int) -> None:
        nonlocal ans

        if node.left is None and node.right is None:  # is None
            return

        if ans.index(ans[-1], -1) < i:
            ans += [[0, 0]]  # ans[i+1] - for children node i + 1

        for ch in [node.left, node.right]:

            if ch:
                ans[i][0] += ch.val
                ans[i][1] += 1
                dfs(ch, i + 1)

    ans = [[root.val, 1]]  # list размером в кол-во слоев, i - level number from 0
    dfs(root, 1)
    ans = [s / c if c else 999 for j, (s, c) in enumerate(ans)]

    return ans


test_data = [
    ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
    ([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000]),
    ([3, 1, 4, 3, None, 1, 5], [3., 2.5, 3.]),
    ([3, 3, None, 4, 2], [3., 3., 3.]),
    ([1], [1]),
    ([3], [3]),
]
f_l = [average_of_levels_dfs]


@pytest.mark.parametrize('root, expected', test_data)
def test(root, expected):
    for i, f in enumerate(f_l):
        ans = f(root)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        n -= 0 if n % 2 else 1
        root = [random.randint(-A_MAX, A_MAX) for i in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.05111516800025129


# -------------------------------

# # TO README
def test_readme():
    topic = 'Tree'
    file_name = 'average_of_levels_in_binary_tree_637.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|637 | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/easy/average_of_levels_in_binary_tree_637.py) | Easy|

"""
