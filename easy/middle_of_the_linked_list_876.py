import time
import pytest
import random

"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

N_MAX = int(1e2)
X_MAX = 100


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # contains the data
        self.next = next  # contains the reference to the next node


# Creatively redesigned code from https://stackoverflow.com/questions/280243/python-linked-list
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = ListNode(val, self.head)  # create a new node
        self.head = new_node                 # set the current node to the new one.

    def __str__(self):
        node = self.head
        _str = ''  # [1->2, 2->3, 3->4, 4->5, 5->None]
        while node:
            _str += f'{node.val}->'
            node = node.next
        return _str + 'None'


def bild_linked_list(arr: list):
    """ Bild the singly linked list """

    llist = LinkedList()
    for x in reversed(arr):
        llist.add_node(x)
    return llist


def middle_node(arr: list, is_debug=False) -> LinkedList:
    """ Return the middle node of the singly linked list """
    llist = bild_linked_list(arr)
    head = llist.head

    fast = head
    slow = head

    if is_debug:
        print(f'\n{arr}')
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if is_debug:
            print(f'fast: {fast.val}, slow: {slow.val}' if fast else f'fast: {fast}, slow: {slow.val}')

    llist.head = slow  # for compatibility to my LinkedList and tests
    if is_debug:
        print(f'Linked list: {llist}')
    return llist  # slow -> to leetcode.com


test_data = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ([1, 2], [2]),
    (list(range(1, 10)) * 2, list(range(1, 10))),
    (list(range(1, 11)) * 2, list(range(1, 11)))
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    f = middle_node
    data = f(arr)
    expected = bild_linked_list(expected)
    node1 = data.head
    node2 = expected.head

    while node1 and node2:
        assert node1.val == node2.val
        node1 = node1.next
        node2 = node2.next


def test_time(n_iter=100):
    f = middle_node
    acc = 0
    for _ in range(n_iter):
        arr = [random.randint(1, X_MAX) for _ in range(1, N_MAX + 1)]
        t0 = time.perf_counter()
        f(arr)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)

    print(acc)  # 5e-5

    assert acc < 0.1
