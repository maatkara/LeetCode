from random import randint

import pytest

from utils.linked_list import *

string_ = """
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
Medium

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the node that 
tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
------------------
circularlinkedlist_test142_1.png

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
------------------
circularlinkedlist_test142_2.png

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
------------------
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
------------------
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Solution:
-----------------------------------------
Floyd's tortoise and hare algorithm.
-----------------------------------------
Floyd's cycle-finding algorithm is a pointer algorithm that uses two pointers ("tortoise" and "hare"), 
which move through the sequence at different speeds.

If there is no cycle, then the hare and the tortoise will never meet. 
Otherwise, if after the meeting of the hare and the turtle at point i, one more turtle is released from the start,
then our turtles will meet at μ - the starting point of the cycle. 
λ - cycle length, μ - starting point of the cycle (pos)
 
solution142.png

Time complexity: O(n),
Space complexity: O(1)

04.01.23
"""
N_MAX = int(1e4)
N_MIN = 0
A_MAX = int(1e5)
A_MIN = -int(1e5)


def detect_cycle(llist: list, pos: int = -1) -> Optional[ListNode]:
    """ Floyd Cycle detection algorithm """

    # only for testing/ not for LC
    head = bild_cycled_llist(llist, pos)
    # ----------------------

    if not head or not head.next:
        return None

    slow = head.next
    fast = head.next.next

    # To the hare and turtle meeting point i
    while fast and fast.next and fast != slow:
        fast = fast.next.next
        slow = slow.next

    # No meeting - no cycle
    if slow != fast:
        return None

    # Find the position μ - the starting point of the cycle
    # and meeting place for our turtles
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow


a_l = [randint(A_MIN, A_MAX) for i in range(N_MAX)]
test_data = [
    ([3, 2, 0, -4], 1, [2, 0, -4]),

    ([3, 2, 0, -4], 2, [0, -4]),
    ([3, 2, 0], 1, [2, 0]),
    ([1, 2], 0, [1, 2]),
    ([1, 2], 1, [2]),
    ([1, 2], -1, None),
    ([1], -1, None),
    ([], -1, None),
    ([], 5, None),
    ([3, 2, 0, -4], -1, None),
    (a_l, N_MAX // 2, a_l[N_MAX // 2:]),
    (a_l, 2, a_l[2:]),
    (a_l, -1, None)

]

f_l = [detect_cycle]


@pytest.mark.parametrize('llist, pos, expected', test_data)
def test(llist: list, pos, expected: list):
    for i, f in enumerate(f_l):
        ans = f(llist, pos)
        expected = bild_linked_list(expected)
        print('\n', f.__name__, ans.val if ans else 'None')

        if not expected:
            assert ans == expected
        else:
            head_exp = expected

            while expected:
                assert ans.val == expected.val
                ans = ans.next
                expected = expected.next

            assert ans.val == head_exp.val


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint
    import numpy as np

    def get_args(i: int,
                 n_max: int = N_MAX, a_max: int = A_MAX,
                 n_min: int = N_MIN, a_min: int = A_MIN,
                 ) -> tuple:
        n = n_max if i == n_iter - 1 else randint(n_min, n_max)
        pos = n_max if i == n_iter - 1 else randint(n_min, n)
        arr = np.random.randint(a_min, a_max, size=n).tolist()

        return arr, pos

    print_time(f_l, get_args, n_iter)


"""
TIME:
                min      mean     max
=========================================
detect_cycle  5.2e-05  4.7e-03  3.2e-02
=========================================
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Linked List'
    file_name = "linked-list-cycle-ii-142.py"

    print('\n')
    print(get_readme(string_, topic, file_name))
