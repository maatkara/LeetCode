import random

import pytest

from utils.binary_tree import BinaryTree, TreeNode

string_ = """
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Medium

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
-------------
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
-------------
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
-------------
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
-------------
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are **unique**.
p != q
p and q will exist in the **BST**.

Time complexity: O(h), h - tree height
Space complexity: O(n) - recursive, O(1) iterative

07.01.23
"""
N_MAX = int(1e5)
N_MIN = 2

A_MAX = int(1e9)
A_MIN = -int(1e9)


def lowest_common_ancestor_rec(root_l: list[int], p: int, q: int) -> TreeNode:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    root = bt.make_tree(root_l)
    left, right = min(q, p), max(q, p)

    # -----------------------------

    # left, right = min(q.val, p.val), max(q.val, p.val)  # for LC

    def dfs(node):

        if left <= node.val <= right:
            return node
        if node.val > right:
            return dfs(node.left)
        if node.val < left:
            return dfs(node.right)

    return dfs(root)


def lowest_common_ancestor_iter(root_l: list[int], p: int, q: int) -> TreeNode:  # submitted
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    root = bt.make_tree(root_l)
    left, right = min(q, p), max(q, p)
    # -----------------------------

    # left, right = min(q.val, p.val), max(q.val, p.val) ! for LC
    cur = root

    while cur:
        if left <= cur.val <= right:
            return cur
        if cur.val > right:
            cur = cur.left
        else:
            cur = cur.right


test_data = [
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ([2, 1], 2, 1, 2),
    ([2, None, 3], 2, 3, 2),
    ([2, None, 3, None, 4, None, 5], 2, 5, 2),
    ([-72, None, 0, None, 4, None, 59, None, 80], -72, 80, -72)

]

f_l = [lowest_common_ancestor_rec, lowest_common_ancestor_iter]


@pytest.mark.parametrize('root_l, p, q, expected', test_data)
def test(root_l: list[int], p: int, q: int, expected: int):
    for f in f_l:
        ans = f(root_l, p, q)
        print('\n', f.__name__, ans)

        assert ans.val == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        arr = []
        for x in sorted(random.choices(range(A_MIN, A_MAX), k=n)):
            arr.extend((x, None))

        arr = arr[:-1]
        p, q = arr[0], arr[-1]
        return arr, p, q

    print_time(f_l, get_args, n_iter)


"""
TIME:
                               min      mean     max
========================================================
lowest_common_ancestor_rec   1.8e-04  6.4e-02  1.5e-01
lowest_common_ancestor_iter  1.5e-04  6.2e-02  1.3e-01  sub
========================================================

"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name = 'lowest-common-ancestor-of-a-binary-search-tree-235.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
