from typing import Optional

import pytest

from utils.linked_list import ListNode, bild_linked_list

string_ = """
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
------------------------
remove_node_ll_19.jpg
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
------------------------
Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
------------------------
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?

28.9.22
"""
N_MAX = 30
N_MIN = 1

A_MIN = 0
A_MAX = 100


def remove_nth_from_end(head_l: list, n: int) -> Optional[ListNode]:
    # only for testing/ not for LC
    head = bild_linked_list(head_l)
    # ----------------------
    # print(head)

    fast = head
    slow = head
    i = 0

    while fast:

        fast = fast.next
        if i > n:
            slow = slow.next
        i += 1

    if i == 1:  # Only 1 node in the initial Linked List
        return None

    if i > n:
        slow.next = slow.next.next
        return head

    return slow.next  # Remove first node => head to next one


test_data = [
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ([1, 2, 3, 4, 5], 4, [1, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], 2, [1, 2, 3, 4, 6]),
    ([1], 1, []),
    ([1, 2], 1, [1])

]

f_l = [remove_nth_from_end]


@pytest.mark.parametrize('head_l, n, expected', test_data)
def test(head_l, n, expected):
    for i, f in enumerate(f_l):

        node1 = f(head_l, n)
        node2 = bild_linked_list(expected)
        print('\n', f.__name__, node1.val if node1 else 'None')

        while node2:
            assert node1.val == node2.val
            node1 = node1.next
            node2 = node2.next

        assert node1 is None


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN,
                 ) -> tuple:
        sz = n_max if i == n_iter - 1 else randint(n_min, n_max)
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        list1 = np.random.randint(a_min, a_max, size=sz).tolist()

        return list1, n

    print_time(f_l, get_args, n_iter)


"""
TIME:
                       min      mean     max
================================================
remove_nth_from_end  1.4e-06  1.0e-05  2.3e-05
================================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Linked List'
    file_name = 'remove-nth-node-from-end-of-list-19.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
