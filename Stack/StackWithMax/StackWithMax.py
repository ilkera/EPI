# Problem: Implement a Stack with MAX Api.

# Stack

# Exception Class
class StackUnderFlowError(Exception):
    def __init__(self, value):
       self.value = value
    def __str__(self):
        return repr(self.value)

class StackWithMax:
    data_stack = None
    max_stack = None

    #constructor
    def __init__(self, capacity):
        self.data_stack = Stack(capacity)
        self.max_stack = Stack(capacity)

    def push(self, item):
        if self.data_stack.isFull():
            raise OverflowError("Stack is full")

        if self.max_stack.isEmpty() or item >= self.max_stack.top():
            self.max_stack.push(item)
        self.data_stack.push(item)

    def pop(self):
        if self.data_stack.isEmpty():
            raise StackUnderFlowError("Stack is empty")

        popped = self.data_stack.pop()
        if popped == self.max_stack.top():
            self.max_stack.pop()
        return popped

    def length(self):
        return self.data_stack.length()

    def top(self):
        return self.data_stack.top()

    def max(self):
        return self.max_stack.top()

    def isEmpty(self):
        return self.data_stack.isEmpty()

    def isFull(self):
        return self.data_stack.isFull()

    def capacity(self):
        return self.data_stack.capacity()

    def clear(self):
        self.data_stack.clear()
        self.max_stack.clear()

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

class StackWithMaxUnitTests(unittest.TestCase):

    def test_maxIsUpdatedAfterPush(self):
        s = StackWithMax(3)
        s.push(5)
        self.assertEqual(5, s.max())
        s.push(12)
        self.assertEqual(12, s.max())
        s.push(15)
        self.assertEqual(15, s.max())

    def test_maxIsKeptIfItemIsLessThanMaxIsInserted(self):
        s = StackWithMax(3)
        s.push(5)
        self.assertEqual(5, s.max())
        s.push(12)
        self.assertEqual(12, s.max())
        s.push(7)
        self.assertEqual(12, s.max())

    def test_maxIsRemovedAfterPop(self):
        s = StackWithMax(3)
        s.push(5)
        self.assertEqual(5, s.max())
        s.push(12)
        self.assertEqual(12, s.max())
        s.pop()
        self.assertEqual(5, s.max())

    def test_maxRaisesExceptionIfStackIsEmpty(self):
        s = StackWithMax(3)
        try:
            max = s.max()
        except StackUnderFlowError as inst:
            self.assertEqual(type(inst), type(StackUnderFlowError("test")))

    def test_duplicateMaxItemsNotRemovedAfterPopup(self):
        s = StackWithMax(3)
        s.push(5)
        self.assertEqual(5, s.max())
        s.push(5)
        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(5, s.max())


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