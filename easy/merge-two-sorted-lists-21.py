from typing import Optional

import pytest

from utils.linked_list import bild_linked_list, ListNode

string_ = """
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Easy

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
----------------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
----------------
Input: list1 = [], list2 = []
Output: []

Example 3:
----------------
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
----------------
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Time complexity: O(min(n, m))
Space complexity: O(1)
02.01.23
"""
N_MAX = 50
N_MIN = 0
A_MAX = int(1e2)
A_MIN = -int(1e2)


def merge_two_lists(llist1: list, llist2: list) -> Optional[ListNode]:
    # only for testing/ not for LC
    list1 = bild_linked_list(llist1)
    list2 = bild_linked_list(llist2)
    # ----------------------

    dummy = ListNode(None)
    prev = dummy

    while list1 and list2:
        if list1.val > list2.val:
            prev.next = list2
            list2 = list2.next
        else:
            prev.next = list1
            list1 = list1.next

        prev = prev.next

    if list1:
        prev.next = list1

    if list2:
        prev.next = list2

    return dummy.next


test_data = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    (sorted(list(range(A_MIN, A_MAX, (A_MAX - A_MIN) // N_MAX))),
     sorted(list(range(A_MIN + 1, A_MAX + 1, (A_MAX - A_MIN) // N_MAX))),
     sorted(list(range(A_MIN, A_MAX, (A_MAX - A_MIN) // N_MAX)) +
            list(range(A_MIN + 1, A_MAX + 1, (A_MAX - A_MIN) // N_MAX))))
]

f_l = [merge_two_lists]


@pytest.mark.parametrize('llist1, llist2, expected', test_data)
def test(llist1: list, llist2: list, expected: list):
    for i, f in enumerate(f_l):
        ans = f(llist1, llist2)
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
        sz2 = n_max if i == n_iter - 1 else randint(n_min, n_max)
        list1 = np.random.randint(a_min, a_max, size=sz1).tolist()
        list2 = np.random.randint(a_min, a_max, size=sz2).tolist()

        return list1, list2

    print_time(f_l, get_args, n_iter)


"""
N_MAX = 50
TIME:
                   min      mean     max
============================================
merge_two_lists  1.6e-06  2.2e-05  5.5e-05
============================================
O(n) ~ 1e-6
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Linked List'
    file_name = "merge-two-sorted-lists.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
