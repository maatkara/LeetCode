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

        self.root = root_l[0] if root_l else None

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


def tree_by_level_coord(root: TreeNode, step=2) -> defaultdict:
    """

    :param root:
    :param step:
    :return:  root_levels[level]: tuple(r, c, val)
    """
    r, c = 0, 0
    root_levels = defaultdict(list)
    root_levels[0] = [[c, root.val]]

    def dfs(node: TreeNode, i=0, c=0):
        nonlocal root_levels

        if not node:
            return

        c_par = c
        for j, ch in enumerate([node.left, node.right]):
            c = c_par + (step + 3 * (not i)) * (2 * j - 1)  # step + (not i) -  around root: step + 1
            root_levels[i + 1] += [[c, ch.val]] if ch else [None]
            dfs(ch, i + 1, c)

    dfs(root)

    h_tree = len(root_levels)
    if not set(root_levels[h_tree - 1]).discard(None):
        del root_levels[h_tree - 1]
        h_tree -= 1
    return root_levels


def inorder_traversal(root: TreeNode) -> list:
    def dfs(node: TreeNode):
        return dfs(node.left) + [node.val] + dfs(node.right) if node else []

    return dfs(root)


def preorder_traversal(root: TreeNode) -> list:
    def dfs(node: TreeNode):
        return [node.val] + dfs(node.left) + dfs(node.right) if node else []

    return dfs(root)


def postorder_traversal(root: TreeNode) -> list:
    def dfs(node: TreeNode):
        return dfs(node.left) + dfs(node.right) + [node.val] if node else []

    return dfs(root)


def inorder_traversal_iter(root_l: list) -> list:
    # Bild tree  | only for testing, not for LC
    # ------------------------------
    bt = BinaryTree()
    bt.make_tree(root_l)
    root = bt.root

    # -----------------------------
    if not root:
        return []

    ans = []

    stack = [root]
    cur = root.left

    while stack or cur:

        while cur:
            stack.append(cur)
            cur = cur.left

        node = stack.pop()
        ans += [node.val]
        cur = node.right

    return ans


def inorder_traversal_with_level(root: TreeNode) -> list:
    def dfs(node: TreeNode, is_right=False, is_leaf=False, level=0):
        return (dfs(node.left, level=level + 1) +
                [(node.val, is_right, (node.right is None and node.left is None), level)] +
                dfs(node.right, is_right=True, level=level + 1) if node else []
                )

    return dfs(root)


def print_tree(root: TreeNode, with_projection=True):
    projection = inorder_traversal_with_level(root)

    cur = 0
    str_d, staff_d = defaultdict(str), defaultdict(str)

    for val, is_right, is_leaf, level in projection:

        # val
        si = cur - len(str_d[level])
        su = cur - len(staff_d[level + 1])  # _
        su = 0 if is_leaf or su >= si else su
        str_d[level] += ' ' * (si - su) + '_' * su + str(val)  # val

        # staff
        si = cur - len(staff_d[level])
        if is_right:
            staff_d[level] += ' ' * (si - 1) + '\\'
            str_d[level - 1] += (cur - len(str_d[level - 1]) - 1) * '_'
        else:
            staff_d[level] += ' ' * (si + len(str(val))) + '/'

        cur += len(str(val)) + 1

    staff_d[0] = ''
    for i in range(len(str_d)):
        print(staff_d[i])
        print(str_d[i])
    if with_projection: print(*[val for val, _, _, _ in projection])

    return str_d, staff_d
