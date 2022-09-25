class MyCircularQueue:
    """
    The circular queue is a linear data structure in which the operations are performed
    based on FIFO (First In First Out) principle and the last position is connected back
    to the first position to make a circle.

    It is also called Ring Buffer.
    """

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0

    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def de_queue(self) -> bool:
        if self.is_empty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.front]

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.rear - 1]  # -1: We have already moved self.rear to the next one

    def is_empty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def is_full(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None
