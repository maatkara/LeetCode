import random

import pytest

from utils.binary_tree import BinaryTree

string_ = """
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

Example 1:
------------------
Input: root = [2,1,3]
Output: true

Example 2:
------------------
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
------------------
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

Time complexity: O(n)
Space complexity: O(n)

06.01.23
"""
N_MAX = int(1e4)
N_MIN = 1

A_MAX = 2 ** 31 - 1
A_MIN = - 2 ** 31


def is_valid_bst(root_l: list[int]) -> bool:
    """ Check BST property: All key left subtree < node.key < all key right subtree """

    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    root = bt.make_tree(root_l)

    # -----------------------------
    if not root:
        return True

    min_v = -float('inf')
    stack = [root]
    cur = root.left

    while stack or cur:

        while cur:
            stack.append(cur)
            cur = cur.left

        node = stack.pop()
        if node.val <= min_v:
            return False

        min_v = node.val
        cur = node.right

    return True


test_data = [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),

    ([1, 2, 3], False),
    ([], True),
    ([2, None, 5, 3, None, None, 5], False),

]

f_l = [is_valid_bst]


@pytest.mark.parametrize('root_l, expected', test_data)
def test(root_l: list[int], expected: bool):
    for f in f_l:
        ans = f(root_l)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

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
=========================================
is_valid_bst  9.2e-05  4.0e-03  2.8e-02
=========================================

"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name = 'validate-binary-search-tree-98.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
