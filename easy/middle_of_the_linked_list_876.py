import random
import time
from typing import Optional

import pytest

from utils.linked_list import bild_linked_list, ListNode

"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
Easy

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
--------------
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
--------------
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
--------------
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

18.8.2021
"""

N_MAX = int(1e2)
X_MAX = 100


def middle_node(arr: list) -> Optional[ListNode]:
    """ Return the middle node of the singly linked list """
    head = bild_linked_list(arr)  # for testing only | not for LC
    # ---------------------------

    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


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
    node1 = f(arr)
    node2 = bild_linked_list(expected)

    while node2:
        assert node1.val == node2.val
        node1 = node1.next
        node2 = node2.next

    assert node1 is None


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
