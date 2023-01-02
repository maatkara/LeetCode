import random
import time

import pytest

from utils.linked_list import *

"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Easy


Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
22.08.2022
"""
N_MAX = 5000
X_MAX = 5000  # +-


def reverse_list(arr: list, is_debug=True) -> LinkedList:
    # only for testing/ not for LC
    head = bild_linked_list(arr)
    # -----------------

    if is_debug:
        print(f'\n{arr}')

    # Turn head to reverse
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt
        if is_debug:
            print(f'prev: {prev.val}, cur: {cur.val}' if cur else f'prev: {prev.val}, cur: {cur}')

    if is_debug:
        print(f'Linked list: {prev}')

    return prev


a_l = [random.randint(-X_MAX, X_MAX) for _ in range(1, N_MAX + 1)]
test_data = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
    ([1, 2], [2, 1]),
    ([], []),
    (a_l, [x for x in reversed(a_l)])
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    f = reverse_list
    is_debug = True if len(arr) <= 20 else False
    node1 = f(arr, is_debug=is_debug)
    node2 = bild_linked_list(expected)

    while node2 or node1:
        assert node1.val == node2.val
        node1 = node1.next
        node2 = node2.next


def test_time(n_iter=100):
    f = reverse_list
    acc = 0
    for _ in range(n_iter):
        arr = [random.randint(-X_MAX, X_MAX) for _ in range(1, N_MAX + 1)]
        t0 = time.perf_counter()
        f(arr, is_debug=False)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)

    print('\n', acc)  # 0.04

    assert acc < 0.1
