import random
import time
from collections import defaultdict
from heapq import heapify, heappush, heappop
from itertools import groupby

import pytest

from utils.binary_tree import BinaryTree, TreeNode
from utils.make_string import get_readme

string_ = """
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Hard

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions 
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index
starting from the leftmost column and ending on the rightmost column.
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
 

Example 1:
--------------------
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
--------------------
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
--------------------
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 
Constraints:
--------------------
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

Solution:
-----------------
1. 
   d_col = def_d([]) 
   d_col[col] = [(r, node_i.var), (node_j.var)] 
   
2. ans: []   ans <- d_col, heapsort
  
4.9.22
"""

N_MAX = int(1e3)
A_MAX = int(1e3)


def heapsort(col_l: list):
    heapify(col_l)
    return [heappop(col_l)[-1] for _ in range(len(col_l))]


def heapsort1(h):
    return [heappop(h) for _ in range(len(h))]


def grouper(item):
    return item[0]


def vertical_traversal(root_l: list) -> list:
    """ Submitted to  LC"""

    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # -----------------------------

    d_col = defaultdict(list)
    d_col[0] = [(0, root.val)]

    def dfs(node: TreeNode, r_par, c_par) -> int:
        nonlocal d_col

        if not node.left and not node.right:
            return

        r = r_par + 1

        for i, ch in enumerate([node.left, node.right]):

            if ch:
                c = c_par + 1 * (2 * i - 1)
                d_col[c].append((r, ch.val))
                dfs(ch, r, c)

    dfs(root, 0, 0)
    return [heapsort(d_col[c]) for c in sorted(d_col.keys())]


def vertical_traversal_h(root_l: list) -> list:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root
    # -----------------------------

    h = [(0, 0, root.val)]
    heapify(h)

    def dfs(node: TreeNode, r_par, c_par) -> int:
        nonlocal h

        if not node.left and not node.right:
            return

        r = r_par + 1

        for i, ch in enumerate([node.left, node.right]):
            if ch:
                c = c_par + 1 * (2 * i - 1)
                heappush(h, (c, r, ch.val))
                dfs(ch, r, c)

    dfs(root, 0, 0)
    h = heapsort1(h)

    return [[t[-1] for t in val] for _, val in groupby(h, key=grouper)]


test_data = [
    ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
    ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
    ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
    ([1], [[1]]),
    ([1, 2, None], [[2], [1]]),
    ([2, -2, -5, 2, -2, 4, -1, None, 0, None, 1, None, None, 2, -1, None, 5, None, None, 1, 3, None, None, None, None,
      None, 3, None, -5, 2, -4, None, None, None, -3],
     [[2], [-2, 0], [2, -2, 4, 1, 5, 2], [-5, 1, 2, 3, -3], [-1, 3, -4], [-1, -5]])

]

f_l = [vertical_traversal, vertical_traversal_h]


@pytest.mark.parametrize('root_l, expected', test_data)
def test(root_l, expected):
    for i, f in enumerate(f_l):
        ans = f(root_l)
        print('\n', f.__name__, ans)
        # for answer in ans:
        #     print(answer)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        m = 100
        n = N_MAX - m if i == n_iter - 1 else random.randint(2, N_MAX + 1 - m)
        root_l = [random.randint(0, A_MAX) for _ in range(n - 3)] + [None] * m
        random.shuffle(root_l)
        root_l = [3] + root_l + [14, 15]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(root_l)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for j, f in enumerate(f_l):
        print(f'\n  {f.__name__}: {acc[j]}')


"""
TIME: 
  vertical_traversal  : 0.0013439980011753505
  vertical_traversal_h: 0.039354375998300384
"""


# -------------------------------


# TO README
def test_readme():
    topic = 'Tree'
    file_name = 'vertical_order_traversal_of_a_binary_tree_987.py'
    print('\n')
    print(get_readme(string_, topic, file_name))


"""
|987 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Tree | [Python](https://github.com/maatkara/LeetCode/blob/main/hard/vertical_order_traversal_of_a_binary_tree_987.py) | Hard|

"""
