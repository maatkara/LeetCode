import pytest

from utils.binary_tree import BinaryTree

string_ = """
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
Medium

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
---------------
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
---------------
Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []

Constraints:
---------------
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

24.9.22
"""
N_MAX = int(5e3)
N_MIX = 0
A_MIN = -1000
A_MAX = 1000


# root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
def path_sum(root_l: list, target_sum) -> list:
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------
    ans = []

    def dfs(node, path, r_sum=target_sum):
        nonlocal ans, target_sum

        if not node:
            if not r_sum:
                ans.append(path)
            return

        path.append(node.val)
        r_sum -= node.val
        dfs(node.left, path.copy(), r_sum)

        if node.left or node.right:
            dfs(node.right, path.copy(), r_sum)

    path = list()
    dfs(root, path)

    return ans


def path_sum_bfs(root_l: list, target_sum) -> list:
    """ Submitted to LC """
    # bild_tree  ! only for testing, not for LC
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------

    if not root:
        return []

    ans = []
    stack = [(root, [root.val], target_sum - root.val)]

    while stack:
        cur, path, r_sum = stack.pop()

        if not cur.left and not cur.right and not r_sum:
            ans.append(path)

        if cur.left:
            stack.append((cur.left, path + [cur.left.val], r_sum - cur.left.val))

        if cur.right:
            stack.append((cur.right, path + [cur.right.val], r_sum - cur.right.val))
    return ans


test_data = [
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
    ([1, 2, 3], 5, []),
    ([1, 2], 0, [])

]

f_l = [path_sum, path_sum_bfs]


@pytest.mark.parametrize('root_l, , target_sum, expected', test_data)
def test(root_l, target_sum, expected):
    for i, f in enumerate(f_l):
        ans = f(root_l, target_sum)
        print('\n', f.__name__, ans)
        for an in ans:
            assert an in expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIX, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                min      mean     max
=========================================
path_sum      4.1e-03  9.5e-03  5.2e-02
path_sum_bfs  4.1e-03  8.4e-03  5.2e-02
"""
# # -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Tree'
    file_name =  'path-sum-ii-113.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
