import random
import time

import pytest

from utils.make_string import get_readme

string_ = """
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Medium

Given a binary tree root, a node X in the tree is named good
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
-----------------
1448_1.png

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
-----------------
1448_1.png

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:
-----------------
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

1.9.22
"""

N_MAX = int(1e5)
A_MAX = int(1e4)  # +-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node val: {self.val}, left: {self.left}, right: {self.right}'


class BinaryTree:
    def __init__(self):
        self.root = None

    def make_tree(self, root_l: list):
        n = len(root_l)
        children = [None] * n  # left child index 

        for i, el in enumerate(root_l):
            #  for not reversed
            if i < n // 2:
                children[i] = 2 * i + 1

        for i, el in enumerate(reversed(root_l)):

            if el is None:
                continue

            node = TreeNode(el)

            j = n - 1 - i

            if children[j] and el:
                node.left = root_l[children[j]]
                node.right = root_l[children[j] + 1]

            root_l[n - i - 1] = node

        self.root = root_l[0]


def good_nodes(root_l: list) -> int:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # -----------------------------

    if not root:
        return 0

    def dfs(node: TreeNode, parent_max) -> int:
        nonlocal ans

        if node is None:
            return

        parent_max = max(node.val, parent_max)

        if node.val == parent_max:
            ans += 1

        dfs(node.left, parent_max)
        dfs(node.right, parent_max)

    ans = 0
    dfs(root, -float('inf'))
    return ans


test_data = [
    ([3, 1, 4, 3, None, 1, 5], 4),
    ([3, 3, None, 4, 2], 3),
    ([3, -10, None, -5, 2], 1),
    ([-3, -10, None, -5, 2], 2),
    ([-3, -10, None, -5, 2], 2),
    ([-3, -10, 1, None, None], 2),
    ([-3, -10, 4, -5, 2], 3),
    ([1], 1),
    ([2, -2, -5, 2, -2, 4, -1, None, 0, None, 1, None, None, 2, -1, None, 5, None, None, 1, 3, None, None, None, None,
      None, 3, None, -5, 2, -4, None, None, None, -3], 7)
]
f_l = [good_nodes]


@pytest.mark.parametrize('root, expected', test_data)
def test(root, expected):
    for i, f in enumerate(f_l):
        ans = f(root)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        n -= 0 if n % 2 else 1
        root = [random.randint(-A_MAX, A_MAX) for i in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.1941108160026488


# -------------------------------
# TO README
def test_readme():
    topic = 'Array'
    file_name = 'pacific_atlantic_water_flow_417.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Array | [Python](https://github.com/maatkara/LeetCode/blob/main/medium/pacific_atlantic_water_flow_417.py) | Medium|

"""
