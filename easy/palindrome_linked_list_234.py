import pytest
import random
import time

from utils.linked_list import *

"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
Easy

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

22.08.2022
"""

N_MAX = 105
X_MAX = 9


def is_palindrome(arr: list, is_debug=True) -> bool:
    """  Return true if singly linked list is a palindrome.

    :param arr: bild_linked_list(arr) -  singly linked list with head in 0-index
          head: head of a singly linked list
    :param is_debug: for printing if debug
    """

    llist = bild_linked_list(arr)  # not for LC
    head = llist.head  # not for LC

    # Find the middle of LL (# 876)
    fast = head
    slow = head

    if is_debug:
        print(f'\n{arr}')

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if is_debug:
            print(f'fast: {fast.val}, slow: {slow.val}' if fast else f'fast: {fast}, slow: {slow.val}')

    # Turn slow to reverse (# 206)
    prev = None
    cur = slow
    #
    while cur:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt

    # Is it an palindrome?
    h1 = head
    h2 = prev

    while h2:
        if h1.val != h2.val:
            return False
        h1 = h1.next
        h2 = h2.next

    return True


a_l = [random.randint(0, X_MAX) for _ in range(0, N_MAX)]
a_lr = [x for x in reversed(a_l)]
test_data = [
    ([1, 2, 2, 1], True),
    ([1, 2, 1], True),
    ([1, 2], False),
    (a_l + a_lr, True),
]


@pytest.mark.parametrize('arr, expected', test_data)
def test(arr, expected):
    is_debug = True if len(arr) <= 20 else False
    f = is_palindrome
    assert f(arr, is_debug=is_debug) == expected


def test_time(n_iter=100):
    f = is_palindrome
    acc = 0
    for _ in range(n_iter):
        arr = [random.randint(0, X_MAX) for _ in range(N_MAX)]
        t0 = time.perf_counter()
        f(arr, is_debug=False)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)

    print('\n', acc)  # 6e-5

    assert acc < 0.1
