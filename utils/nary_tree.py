from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        return f'Node val: {self.val}, children: {self.children}'


class NaryTree:
    """ Nary-Tree input serialization is represented in their level order traversal,
    each group of children is separated by the null value (See examples).

    Example:
        ----------
        [1,null,3,2,4,null,5,6]
           1
         / | \
        3  2  4
          /\
         5  6

    """

    def __init__(self):
        self.root = None
        self.size = 0

    def make_tree(self, root_l: list):
        self.size = len(root_l)

        if not self.size:
            return

        j = 2
        self.root = Node(val=root_l[0])
        q = deque([self.root])

        while q and j < self.size:

            cur = q.popleft()
            ch_l = []

            while j < self.size and root_l[j]:
                node = Node(val=root_l[j])
                q.append(node)
                ch_l.append(node)
                j += 1

            if ch_l:
                cur.children = tuple(ch_l)

            j += 1
