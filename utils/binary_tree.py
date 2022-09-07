from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'val: {self.val}, left: {self.left}, right: {self.right}'


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def make_tree(self, root_l: list):

        root_l = [self.add_node(el) for el in root_l]
        self.size = len(root_l)
        i = 0
        j = 1

        while i < self.size:

            node = root_l[i]

            if node and j < self.size:
                node.left = root_l[j]
                j += 1
                if j < self.size:
                    node.right = root_l[j]
                j += 1
            i += 1

        self.root = root_l[0]

    @staticmethod
    def add_node(x):
        return TreeNode(x) if x is not None else None


def tree_by_level(root: TreeNode) -> defaultdict:
    root_levels = defaultdict(list)
    root_levels[0] = [root.val]

    def dfs(node: TreeNode, i=0):
        nonlocal root_levels

        if not node:
            return

        for ch in (node.left, node.right):
            root_levels[i + 1] += [ch.val] if ch else [None]
            dfs(ch, i + 1)

    dfs(root)
    return root_levels
