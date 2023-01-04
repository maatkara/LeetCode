"""

Linked list implementation.
Creatively redesigned code from https://stackoverflow.com/questions/280243/python-linked-list

Class ListNode, LinkedList
function bild_linked_list(arr: list):    Bild the singly linked list from a list
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # contains the data
        self.next = next  # contains the reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = ListNode(val, self.head)  # create a new node
        self.head = new_node  # set the current node to the new one.

    def __str__(self):
        node = self.head
        _str = ''  # [1->2, 2->3, 3->4, 4->5, 5->None]
        while node:
            _str += f'{node.val}->'
            node = node.next
        return _str + 'None'


def bild_linked_list(arr: list):
    """ Bild the singly linked list from list"""
    if not arr:
        return None

    llist = LinkedList()
    for x in reversed(arr):
        llist.add_node(x)
    return llist.head


def bild_cycled_llist(arr: list, pos: int):
    """ Bild the singly linked list from list"""

    llist = LinkedList()
    start = None
    tail = None

    if not arr:
        return None

    if pos == -1:
        return bild_linked_list(arr)

    if pos >= len(arr):
        print(f"pos {pos} >= len(arr) {len(arr)}")
        return None

    pos = len(arr) - 1 - pos

    for i, x in enumerate(reversed(arr)):
        llist.add_node(x)
        if i == 0:
            tail = llist.head
        if i == pos:
            start = llist.head

    head = llist.head
    # tail = llist.head
    #
    # while tail.next:  # Go to tail
    #     tail = tail.next
    if start and tail:
        tail.next = start

    return head


def print_linked_list(head: Optional[ListNode]): #  , cycle_pos: int=-1
    cur = head
    string_ = ''
    # len_s0 = 0
    # i = 0

    while cur:
        # if i == cycle_pos:
        #     len_s0 = len(string_)
        string_ += f"{cur.val}->"
        cur = cur.next
        # i += 1
    #
    # if cycle_pos != -1:
    #     string1 = ' ' * len_s0 + '^'
    #     string1 += '_' * (len(string_) - len(string1) - 1) + '|'
    #     string_ += '\n' + string1
    # else:
    #     string_ += 'None'

    print(string_ + 'None')
