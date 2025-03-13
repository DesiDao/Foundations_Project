class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        temp = self.top
        self.top = self.top.next
        self._size -= 1
        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
