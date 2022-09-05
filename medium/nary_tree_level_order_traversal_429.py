import random
import time
from collections import defaultdict

import pytest

from utils.make_string import get_readme
from utils.nary_tree import NaryTree, Node

string_ = """
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

 
Example 1:
------------------------
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
------------------------
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:
------------------------
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]


5.9.22
"""
H_MAX = int(1e3)
N_MAX = 104


def level_order_dfs(root_l: list) -> list:
    """Definition for a Node.
       ----------------------
        class Node:
            def __init__(self, val=None, children=None):
                self.val = val
                self.children = children
"""

    # bild tree  ! ONLY FOR TESTING, not for LC
    nt = NaryTree()
    nt.make_tree(root_l)
    root = nt.root
    # -----------------------------

    if not root:
        return []

    levels = [[root.val]]  # levels[level] = [..., node_i.val, ..]

    def dfs(node: Node, level=0):
        nonlocal levels

        if not node.children:
            return

        if len(levels) < level + 2:
            levels += [[]]

        levels[level + 1] += [ch.val for ch in node.children]

        for ch in node.children:
            dfs(ch, level + 1)

    dfs(root)

    return levels


def level_order_dfs_1(root_l: list) -> list:
    """ LC submitted

    Definition for a Node.
       ----------------------
        class Node:
            def __init__(self, val=None, children=None):
                self.val = val
                self.children = children
"""

    # bild tree  ! ONLY FOR TESTING, not for LC
    nt = NaryTree()
    nt.make_tree(root_l)
    root = nt.root
    # -----------------------------

    if not root:
        return []

    levels = defaultdict(list)
    levels[0] = [root.val]  # levels[level] = [..., node_i.val, ..]

    def dfs(node: Node, level=0):

        if not node.children:
            return

        levels[level + 1] += [ch.val for ch in node.children]
        for ch in node.children:
            dfs(ch, level + 1)

    dfs(root)

    return list(levels.values())


test_data = [
    ([], []),
    ([1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]]),
    ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14],
     [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]])

]

f_l = [level_order_dfs, level_order_dfs_1]


@pytest.mark.parametrize('root_l, expected', test_data)
def test(root_l, expected):
    for i, f in enumerate(f_l):
        ans = f(root_l)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        m = H_MAX - 1 if i == n_iter - 1 else random.randint(1, H_MAX - 1)
        n = N_MAX if i == n_iter - 1 else random.randint(0, N_MAX - 1)

        root_l = [random.randint(0, N_MAX * 100) for _ in range(n)] + [None] * m
        random.shuffle(root_l)
        root_l = [3, None] + root_l + [14, 15]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root_l)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for j, f in enumerate(f_l):
        print(f'\n  {f.__name__}: {acc[j]}')


"""
TIME: 
  level_order_dfs: 9.611700079403818e-05
  level_order_dfs_1: 8.303600043291226e-05
"""


# -------------------------------


# TO README
def test_readme():
    topic = 'Tree'
    file_name = 'nary_tree_level_order_traversal_429.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|429 | [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/medium/nary_tree_level_order_traversal_429.py) | Medium|
"""
