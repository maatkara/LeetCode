import random
import time

import pytest

from utils.binary_tree import TreeNode, BinaryTree, tree_by_level
from utils.make_string import get_readme

string_ = """
814. Binary Tree Pruning
https://leetcode.com/problems/binary-tree-pruning/
Medium

Given the root of a binary tree,
return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
-------------------------------
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
-------------------------------
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
-------------------------------
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:
-------------------------------
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.

6.9.22
"""

N_MAX = 200
A_MAX = 1


def prune_tree(root_l: list) -> list:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------

    def dfs(node: TreeNode):

        if not node:
            return False

        ch_sum_l = dfs(node.left)
        if not ch_sum_l:
            node.left = None

        ch_sum_r = dfs(node.right)
        if not ch_sum_r:
            node.right = None

        return bool(ch_sum_l + ch_sum_r + node.val)

    ch_sum = dfs(root)

    # Only for testing,  not for LC
    # ------------------------------
    new_root = tree_by_level(root)
    new_root = [x for val in new_root.values() for x in val]

    while new_root and not new_root[-1]:  # Remove None`s at the end
        new_root.pop()

    return new_root if ch_sum else []  # ! FOR TEST! | root if ch_sum else None |-> for LC


test_data = [
    ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
    ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
    ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
    ([0, None, 0, 1, 1, None, 1, None, 1, None, None, None, None], [0, None, 0, 1, 1, None, 1, None, 1]),
    ([0] * 10, [])
]
f_l = [prune_tree]


@pytest.mark.parametrize('root, expected', test_data)
def test(root, expected):
    for i, f in enumerate(f_l):
        ans = f(root)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        m = 30
        n = N_MAX - m - 1 if i == n_iter - 1 else random.randint(1, N_MAX - m - 1)
        root = [random.randint(0, 2) for _ in range(n)] + [None] * m
        random.shuffle(root)
        root = [1] + root

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.0002


# -------------------------------


# TO README
def test_readme():
    topic = 'Tree'
    file_name = 'binary_tree_pruning_814.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/medium/binary_tree_pruning_814.py) | Medium|

"""
