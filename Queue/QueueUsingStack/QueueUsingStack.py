# Problem: Queue using stack

# Stack definition
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self,item):
        if not self.isFull():
            self.stack.append(item)
            return
        raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        raise Exception("Stack is empty")

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        raise Exception("Stack is empty")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def length(self):
        return len(self.stack)


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.incoming_stack = Stack(capacity)
        self.outgoing_stack = Stack(capacity)

    def enqueue(self, item):
        if not self.isFull():
            self.incoming_stack.push(item)
            return
        raise Exception("Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            if self.outgoing_stack.isEmpty():
                self.popAllFrom(self.incoming_stack, self.outgoing_stack)
            return self.outgoing_stack.pop()
        raise Exception("Queue is empty")

    def first(self):
        if not self.isEmpty():
            if self.outgoing_stack.isEmpty():
                 self.popAllFrom(self.incoming_stack, self.outgoing_stack)
            return self.outgoing_stack.top()
        raise Exception("Queue is empty")

    def isEmpty(self):
        return self.incoming_stack.isEmpty() and self.outgoing_stack.isEmpty()

    def isFull(self):
        return self.incoming_stack.length() + self.outgoing_stack.length() == self.capacity

    def popAllFrom(self, source, target):
        while not source.isEmpty():
            target.push(source.pop())

# Main program
q = Queue(5)

for item in range(0,5):
    print("Pushing %d" %item)
    q.enqueue(item)

print("DEQUEUE")
while not q.isEmpty():
    popped = q.dequeue()
    print("Popping %d" %popped)
