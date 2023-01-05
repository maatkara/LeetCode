import random

import numpy as np
import pytest

from utils.nary_tree import NaryTree

string_ = """
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Easy

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)

Example 1:
------------------
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
------------------
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:
------------------
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.
 
Follow up: Recursive solution is trivial, could you do it iteratively?

Time complexity: O(h), h - the height of the n-ary tree
Space complexity: O(n)

04.01.23
"""
N_MAX = int(1e4)
N_MIN = 0

A_MAX = int(1e4)
A_MIN = 0

H_MAX = 1000  # height of the n-ary tree


def preorder_rec(root_l: list[int]) -> list[int]:
    # bild tree  ! ONLY FOR TESTING, not for LC
    nt = NaryTree()
    nt.make_tree(root_l)
    root = nt.root

    # -----------------------------
    # ans = []

    def dfs(node, ans):

        if not node:
            return ans

        ans += [node.val]
        if node.children:
            for ch in node.children:
                dfs(ch, ans)
        return ans

    return dfs(root, [])


def preorder_iter(root_l: list[int]) -> list[int]:
    # bild tree  ! ONLY FOR TESTING, not for LC
    nt = NaryTree()
    nt.make_tree(root_l)
    root = nt.root
    # -----------------------------

    if not root:
        return []

    ans = []
    stack = [root]

    while stack:
        node = stack.pop()
        ans.append(node.val)

        if node.children:
            stack.extend(reversed(node.children))

    return ans


test_data = [
    ([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4]),
    ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14],
     [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]),

    ([], [])
]

f_l = [preorder_rec, preorder_iter]


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
        arr = np.random.randint(A_MIN, A_MAX, size=n - 2).tolist() if n > 2 else []
        arr += [None] * randint(1, min(H_MAX - 1, n - 1, 1))  # H_MAX - height of the n-ary tree
        random.shuffle(arr)
        arr = [A_MIN, None] + arr

        return arr,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                min      mean     max
=========================================
preorder_rec  4.4e-05  4.4e-03  2.3e-02
preorder_it   4.0e-05  4.4e-03  2.8e-02
=========================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name = "n-ary-tree-preorder-traversal-589" + ".py"

    print('\n')
    print(get_readme(string_, topic, file_name))
