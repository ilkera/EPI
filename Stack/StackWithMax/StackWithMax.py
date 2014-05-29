# Problem: Implement a Stack with MAX Api.

# Stack

# Exception Class
class StackUnderFlowError(Exception):
    def __init__(self, value):
       self.value = value
    def __str__(self):
        return repr(self.value)

class Stack:

    # Variables
    _items = []
    _capacity = 0

    # Constructor
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity

    def push(self, item):
        if not self.isFull():
            self._items.append(item)
        else:
            raise OverflowError("Stack overflow")

    def pop(self):
        if not self.isEmpty():
            popped = self._items.pop()
            return popped
        else:
            raise StackUnderFlowError("Stack is empty")

    def top(self):
        if not self.isEmpty():
            return self._items[-1]
        else:
             raise StackUnderFlowError("Stack is empty")

    def length(self):
       return len(self._items)

    def capacity(self):
        return self._capacity

    def clear(self):
        if not self.isEmpty():
            self._items.clear()

    def isEmpty(self):
        return self.length() == 0

    def isFull(self):
        return self.length() == self.capacity()


# Tests
import unittest

class StackUnitTests(unittest.TestCase):

    def test_EmptyStack(self):
        s = Stack(4)
        self.assertEqual(0, s.length())

    def test_CapacityInitialized(self):
        s = Stack(5)
        self.assertEqual(s.capacity(), 5)

    def test_PushItemIntoEmptyStack(self):
        s = Stack(5)
        self.assertEqual(0, s.length())
        s.push(1)
        self.assertEqual(1, s.length())

    def test_PushCanAcceptUntilCapacityIsFull(self):
        s = Stack(3)
        self.assertEqual(s.capacity(), 3)
        s.push(1)
        s.push(2)
        s.push(3)

        try:
            s.push(4)
        except Exception as inst:
            self.assertEqual(type(inst), type(OverflowError()))
            self.assertEqual(3, s.capacity())
        else:
            print("Unknown exception")

    def test_PopItemFromStack(self):
        s = Stack(5)
        s.push(99)
        self.assertEqual(1, s.length())
        popped = s.pop()
        self.assertEqual(0, s.length())
        self.assertEqual(99, popped)

    def test_PopFromEmptyStackRaiseException(self):
        s = Stack(5)
        self.assertEqual(0, s.length())

        try:
             popped = s.pop()
        except Exception as inst:
             self.assertEqual(type(inst), type(StackUnderFlowError("test")))
             self.assertEqual(0, s.length())

    def test_LastItemIsPoppedFirst(self):
        s = Stack(5)
        s.push(5)
        s.push(4)
        s.push(3)
        popped = s.pop()
        self.assertEqual(3, popped)
        self.assertEqual(2, s.length())

        popped = s.pop()
        self.assertEqual(4, popped)
        self.assertEqual(1, s.length())

        popped = s.pop()
        self.assertEqual(5, popped)
        self.assertEqual(0, s.length())

    def test_TopReturnsLastInsertedItem(self):
        s = Stack(4)
        s.push(45)
        s.push(20)
        top = s.top()
        self.assertEqual(20, top)
        self.assertEqual(2, s.length())

    def test_TopRaisesExceptionWhenStackIsEmpty(self):
        s = Stack(4)

        try:
            top = s.top()
        except StackUnderFlowError as inst:
            self.assertEqual(type(inst), type(StackUnderFlowError("test")))
            self.assertEqual(0, s.length())

    def test_ClearRemovesAllItems(self):
        s = Stack(5)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(5, s.length())
        s.clear()
        self.assertEqual(0, s.length())

    def test_IsFullReturnsTrueWhenStackIsFull(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertTrue(s.isFull())

    def test_IsEmptyReturnsTrueWhenStackIsEmpty(self):
        s = Stack(3)
        self.assertTrue(s.isEmpty())

# Main Program

if __name__ == '__main__':
    unittest.main()