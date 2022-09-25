import pytest

string_ = """
622. Design Circular Queue
https://leetcode.com/problems/design-circular-queue/
Medium

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) 
principle and the last position is connected back to the first position to make a circle. 
It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even 
if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
Front()         Gets the front item from the queue. If the queue is empty, return -1.
Rear()          Gets the last item from the queue. If the queue is empty, return -1.
enQueue(value)  Inserts an element into the circular queue. Return true if the operation is successful.
deQueue()       Deletes an element from the circular queue. Return true if the operation is successful.
isEmpty()       Checks whether the circular queue is empty or not.
isFull()        Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
--------------------
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

Constraints:
--------------------
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull

25.9.22
"""
N_MAX = int(1e3)
N_MIX = 0
A_MIN = 0
A_MAX = 1000


class MyCircularQueue:
    """
    The circular queue is a linear data structure in which the operations are performed based on FIFO
    (First In First Out) principle and the last position is connected back to the first position to make a circle.

    It is also called "Ring Buffer".
    """

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:  # CamelCase: LC requirement
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]  # -1: We have already moved self.rear to the next one

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None


def dispatcher(queries: list, val_l: list) -> list:
    """ Only For testing """
    ans = [None] * len(queries)

    q = MyCircularQueue(val_l[0][0])

    for i, (query, val) in enumerate(zip(queries[1:], val_l[1:])):
        ans[i + 1] = getattr(q, query)(val[0]) if val else getattr(q, query)()

    return ans


test_data = [
    (["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
     [[3], [1], [2], [3], [4], [], [], [], [4], []],
     [None, True, True, True, False, 3, True, True, True, 4]),

]

f_l = [dispatcher]


@pytest.mark.parametrize('queries, val_l, expected', test_data)
def test(queries, val_l, expected):
    for i, f in enumerate(f_l):
        ans = f(queries, val_l)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=N_MIX, a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
              min      mean     max
=======================================
dispatcher  5.0e-06  3.1e-04  1.4e-03
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Design, Queue'
    file_name = 'design-circular-queue-622.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
