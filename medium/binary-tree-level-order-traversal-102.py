import random
from collections import defaultdict
from typing import Optional

import numpy as np
import pytest

from utils.binary_tree import BinaryTree, TreeNode

string_ = """
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
Medium

Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
---------------------
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
---------------------
Input: root = [1]
Output: [[1]]

Example 3:
---------------------
Input: root = []
Output: []
 

Constraints:
---------------------
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

Time complexity: O(h), h - the height of the n-ary tree
Space complexity: O(n)

05.01.23
"""
N_MAX = int(2e3)
N_MIN = 0

A_MAX = int(1e3)
A_MIN = -int(1e3)


def level_order(root_l: Optional[list[int]]) -> list[list[int]]:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    root = bt.make_tree(root_l)

    # -----------------------------
    level_d = defaultdict(list)

    def dfs(node: TreeNode, level=0):
        nonlocal level_d

        if not node:
            return

        level_d[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

        return

    dfs(root)

    return list(level_d.values())


test_data = [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ([3, 9, 20, -6, -12, 15, 7], [[3], [9, 20], [-6, -12, 15, 7]]),
    ([3, 9, 20, -6, -12, 15, 7, -77, 45, 53, 22, 77, 99, 1, 0], [[3], [9, 20], [-6, -12, 15, 7],
     [-77, 45, 53, 22, 77, 99, 1, 0]]),
    ([1], [[1]]),
    ([], []),
]

f_l = [level_order]


@pytest.mark.parametrize('root_l, expected', test_data)
def test(root_l: list, expected: list):
    for i, f in enumerate(f_l):
        ans = f(root_l)
        print('\n', f.__name__, ans)

        assert len(ans) == len(expected)

        for val, ex in zip(ans, expected):
            assert val == ex


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        n_null = randint(1, max((n - 1) // 10, 2))
        arr = np.random.randint(A_MIN, A_MAX, size=n - n_null - 1).tolist() if n - n_null > 1 else []
        arr += [None] * n_null
        random.shuffle(arr)
        arr = [A_MIN] + arr

        return arr,

    print_time(f_l, get_args, n_iter)


"""
TIME:
               min      mean     max
========================================
level_order  9.8e-06  1.1e-03  1.7e-02
========================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name = "binary-tree-level-order-traversal-102.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
