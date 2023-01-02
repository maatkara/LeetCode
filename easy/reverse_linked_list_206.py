import random
from typing import Optional

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
02.01.23 change testing functions
"""
N_MAX = 5000
N_MIN = 0

A_MAX = 5000
A_MIN = -5000


def reverse_list(arr: list, is_debug=False) -> Optional[ListNode]:
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


f_l = [reverse_list]
a_l = [random.randint(A_MIN, A_MAX) for _ in range(1, N_MAX + 1)]

test_data = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
    ([1, 2], [2, 1]),
    ([], []),
    (a_l, [x for x in reversed(a_l)])
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    for i, f in enumerate(f_l):
        ans = f(arr)
        expected = bild_linked_list(expected)
        print('\n', f.__name__, ans.val if ans else 'None')

        while expected:
            assert ans.val == expected.val
            ans = ans.next
            expected = expected.next

        assert ans is None


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN,
                 ) -> tuple:
        sz1 = n_max if i == n_iter - 1 else randint(n_min, n_max)
        list1 = np.random.randint(a_min, a_max, size=sz1).tolist()

        return list1,

    print_time(f_l, get_args, n_iter)


"""
TIME:
                min      mean     max
=========================================
reverse_list  4.5e-06  2.0e-03  2.7e-02
=========================================

O(n) ~ 1e-4
"""
