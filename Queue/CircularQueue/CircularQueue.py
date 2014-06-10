# Problem: Implement a circular queue

# Circular Queue definition
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, item):
        if not self.isFull():
            self.rear = self.increment(self.rear)
            self.queue[self.rear] = item
            self.count += 1
            return
        raise Exception("Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            popped = self.queue[self.front]
            self.front = self.increment(self.front)
            self.count -= 1
            return popped
        raise Exception("Queue is empty")

    def first(self):
         if not self.isEmpty():
            return self.queue[self.front]
         raise Exception("Queue is empty")

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def clear(self):
        self.count = 0
        self.front = 0
        self.rear = -1

    def increment(self, index):
        if index + 1 == self.capacity:
            index = 0
        else:
            index += 1
        return index

# Unit tests
import unittest
class CircularQueueTests(unittest.TestCase):
    def test_IsEmpty(self):
        cq = CircularQueue(5)
        self.assertEqual(cq.isEmpty(), True)
    def test_IsFull(self):
         cq = CircularQueue(3)
         cq.enqueue(1)
         cq.enqueue(2)
         cq.enqueue(3)
         try:
            cq.enqueue(4)
         except Exception as inst:
            print(inst)

    def test_CircularQueue(self):
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        self.assertEqual(q.isFull(), True)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 6)
        self.assertEqual(q.dequeue(), 7)
        self.assertEqual(q.isEmpty(), True)

