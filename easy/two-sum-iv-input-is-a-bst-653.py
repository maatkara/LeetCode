from random import randint

import pytest

from utils.binary_tree import BinaryTree, TreeNode

string_ = """
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Easy

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST 
such that their sum is equal to k, or false otherwise.

Example 1:
----------------
Input: root = ([5,3,6,2,4,null,7], k = 9)
Output: true

Example 2:
----------------
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
----------------
The number of nodes in the tree is in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5

26.12.22
"""
N_MAX = int(1e4)
N_MIN = 1

A_MIN = -int(1e4)
A_MAX = int(1e4)

K_MAX = int(1e5)


def find_target(root_l: list, k: int) -> bool:  # submitted
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # print_tree(root)

    # -----------------------------

    def dfs(node: TreeNode, nodes):
        nonlocal k

        if not node:
            return False

        if k - node.val in nodes:
            return True

        nodes.add(node.val)
        return dfs(node.left, nodes) or dfs(node.right, nodes)

    return dfs(root, set())


test_data = [
    ([5, 3, 6, 2, 4, None, 7], 9, True),
    ([5, 3, 6, 2, 4, None, 7], 28, False),

    ([5], 5, False),
    ([2, 7, 11, 15], 9, True),
    ([2, 3, 4], 6, True),
    ([-1, 0], -1, True),
    ([3, 3], 6, True),
    ([3, 3, 4], 6, True),

    ([2, 2, 2], 6, False),
    ([2, 2, 3, 3], 6, True),

    ([0] * 10, 2, False),
    (sorted(randint(A_MIN, A_MAX) for _ in range(N_MAX)), K_MAX, False),
]

f_l = [find_target]


@pytest.mark.parametrize('root_l, k, expected', test_data)
def test(root_l, k, expected):
    for i, f in enumerate(f_l):
        ans = f(root_l, k)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIN, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
               min      mean     max
========================================
find_target  2.3e-01  2.5e-01  3.0e-01
========================================

O(n^2) = 1e-9 * N_MAX**2 ~ 1e-1
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name = 'two-sum-iv-input-is-a-bst-653.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
