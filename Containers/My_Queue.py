class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self._size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size
