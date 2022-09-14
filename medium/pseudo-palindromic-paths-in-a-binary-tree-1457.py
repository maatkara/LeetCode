import pytest

from utils.binary_tree import BinaryTree, TreeNode
from utils.make_string import get_readme

string_ = """
1457. Pseudo-Palindromic Paths in a Binary Tree
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
Medium

Given a binary tree where node values are digits from 1 to 9. 
A path in the binary tree is said to be pseudo-palindromic 
if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
 

Example 1:
--------------------
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation:
The figure above represents the given binary tree.
There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], 
and the path [2,3,1]. 
Among these paths only red path and green path are pseudo-palindromic paths since 
the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and 
the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
--------------------
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: 
The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: 
the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. 
Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
--------------------
Input: root = [9]
Output: 1
 

Constraints:
--------------------
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9

14.9.22
"""
N_MAX = int(1e5)
A_MAX = 9


def pseudo_palindromic_paths(root_l: list) -> int:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # -----------------------------

    def dfs(node: TreeNode, values: set):

        if not node:
            return 0

        if node.val in values:
            values.remove(node.val)
        else:
            values.add(node.val)

        if not node.left and not node.right:  # leaf
            return len(values) <= 1

        left = dfs(node.left, values.copy())
        right = dfs(node.right, values.copy())

        return left + right

    return int(dfs(root, set()))


f_l = [pseudo_palindromic_paths]
test_data = [
    ([2, 3, 1, 3, 1, None, 1], 2),
    ([2, 1, 1, 1, 3, None, None, None, None, None, 1], 1),
    ([9], 1),
    ([2, 3, 1, 3, 1, None, 1], 2),
    ([2, 1, None], 0),
    ([2, 1, None, 2, None, 2], 0),
    ([2, 1, None, 2, None], 1),
]


@pytest.mark.parametrize('root_l, expected', test_data)
def test(root_l: list, expected):
    for i, f in enumerate(f_l):
        ans = f(root_l)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    import random
    import time

    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        root_l = [random.randint(1, A_MAX) for _ in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root_l)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.175


# -------------------------------


# TO README
def test_readme():
    topic = 'Bit manipulation'
    file_name = 'pseudo-palindromic-paths-in-a-binary-tree-1457' + 'py'
    print('\n')
    print(get_readme(string_, topic, file_name))
