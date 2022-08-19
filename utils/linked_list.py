"""

Linked list implementation.
Creatively redesigned code from https://stackoverflow.com/questions/280243/python-linked-list

Class ListNode, LinkedList
function bild_linked_list(arr: list):    Bild the singly linked list from a list
"""


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

    llist = LinkedList()
    for x in reversed(arr):
        llist.add_node(x)
    return llist
