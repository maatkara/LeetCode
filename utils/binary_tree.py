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
