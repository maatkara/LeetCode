import random
import time

import pytest

from utils.binary_tree import TreeNode, BinaryTree
from utils.make_string import get_readme

string_ = """
606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/
Easy

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree
with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship
between the string and the original binary tree.


Example 1:
---------------------------
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
---------------------------
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example,
except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship
between the input and the output.
 

Constraints:
---------------------------
The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000

7.9.22
"""

N_MAX = int(1e4)
A_MAX = 1000


def tree2str(root_l: list) -> str:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------

    def dfs(node: TreeNode):

        if not node:
            return ''

        string_ = f'{node.val}'

        if not node.left and not node.right:
            return string_

        string_ += f'({dfs(node.left)})'
        if node.right:
            string_ += f'({dfs(node.right)})'

        return string_

    return dfs(root)


test_data = [
    ([1, 2, 3, 4], "1(2(4))(3)"),
    ([1, 2, 3, None, 4], "1(2()(4))(3)"),
    ([1, 2, -3, None, -4], "1(2()(-4))(-3)"),
    ([1, None, 2, 3, 4], '1()(2(3)(4))'),
    ([0, None, 10, 2, 3, 4], "0()(10(2(4))(3))"),
    ([0, None, 10, 2, 3, None, 4, None, 5, None, None, None, None], "0()(10(2()(4))(3()(5)))"),
    ([0], '0')
]
f_l = [tree2str]


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
        n = N_MAX - m - 1 if i == n_iter - 1 else random.randint(1, N_MAX - m - 1)
        root = [random.randint(-A_MAX, A_MAX) for _ in range(n)] + [None] * m
        random.shuffle(root)
        root = [1] + root

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.04849284199917747


# # -------------------------------


# TO README
def test_readme():
    topic = 'Tree'
    file_name = 'construct_string_from_binary_tree_606.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|606 | [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/easy/construct_string_from_binary_tree_606.py) | Easy|
"""
