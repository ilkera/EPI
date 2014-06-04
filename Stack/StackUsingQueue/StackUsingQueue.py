# Problem: Stack using queue

# Queue Definition
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def enqueue(self, item):
        if not self.isFull():
            self.items.append(item)
            return
        raise Exception("Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        raise Exception("Queue is empty")

    def first(self):
        if not self.isEmpty():
            return self.items[0]
        raise Exception("Queue is empty")

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def length(self):
        return len(self.items)

# Stack with using queue

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = Queue(capacity)
        self.temp = Queue(capacity)

    def push(self, item):
       if not self.isFull():
           if self.queue.isEmpty():
               self.queue.enqueue(item)
           else:
               self.dequeueAll(self.queue, self.temp)
               self.queue.enqueue(item)
               self.dequeueAll(self.temp, self.queue)
       else:
           raise Exception("Stack is full")

    def pop(self):
        if not self.queue.isEmpty():
            return self.queue.dequeue()
        else:
            raise Exception("Stack is empty")

    def top(self):
        if not self.queue.isEmpty():
            return self.queue.first()
        raise Exception("Stack is empty")

    def isEmpty(self):
        return self.queue.length() + self.temp.length() == 0

    def isFull(self):
        return self.queue.length() + self.temp.length() == self.capacity

    def dequeueAll(self, source, dest):
        while not source.isEmpty():
            dest.enqueue(source.dequeue())

# Main program
s = Stack(5)
for item in range(0, 5):
    print("Pushing %d" %item)
    s.push(item)

print("")

while not s.isEmpty():
    print("Popping %d " %s.pop())
