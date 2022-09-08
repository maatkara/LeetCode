import random
import time

import pytest

from utils.binary_tree import TreeNode, BinaryTree
from utils.make_string import get_readme

string_ = """
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.
picture:  94_all_DFS_traversals.png

Example 1:
----------------------
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
----------------------
Input: root = []
Output: []

Example 3:
----------------------
Input: root = [1]
Output: [1]
 

Constraints:
----------------------
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

8.9.22
"""

N_MAX = 100
A_MAX = 100


def inorder_traversal_dfs(root_l: list) -> list:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------

    def dfs(node: TreeNode):
        """ Inorder traversal
        :param node:
        :return: list
        """

        return dfs(node.left) + [node.val] + dfs(node.right) if node else []

    return dfs(root)


def inorder_traversal_iter(root_l: list) -> list:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------
    if not root:
        return []

    ans = []

    stack = [root]
    cur = root.left

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left

        node = stack.pop()
        ans += [node.val]
        cur = node.right

    return ans


test_data = [
    ([1, None, 2, 3], [1, 3, 2]),
    ([], []),
    ([1], [1]),
    ([4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),

    ([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, 10, 11], [4, 2, 8, 5, 1, 6, 9, 3, 10, 7, 11]),
    ([0, None, 10, 2, 3, None, 4, None, 5, None, None, None, None], [0, 2, 4, 10, 3, 5]),
]
f_l = [inorder_traversal_dfs, inorder_traversal_iter]


@pytest.mark.parametrize('root, expected', test_data)
def test(root, expected):
    for i, f in enumerate(f_l):
        ans = f(root)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        m = 0 if i == n_iter - 1 else random.randint(1, N_MAX // 10)
        n = N_MAX - m - 2 if i == n_iter - 1 else random.randint(1, N_MAX - m - 2)
        root = [random.randint(-A_MAX, A_MAX) for _ in range(n)] + [None] * m
        random.shuffle(root)
        root = [1] + root + [5]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.0001280 rec


"""
inorder_traversal_dfs 0.00011447800170572009
inorder_traversal_iter 7.670299964956939e-05
"""


# # -------------------------------


# TO README
def test_readme():
    topic = 'Tree'
    file_name = 'binary_tree_inorder_traversal_94.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/easy/binary_tree_inorder_traversal_94.py) | Easy|

"""
