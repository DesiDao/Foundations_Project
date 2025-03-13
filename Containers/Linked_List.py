class Node:
    def __init__(self, value=None):
        self.value = value  # The data the node stores
        self.next = None  # The reference to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the linked list is empty

    # Method to check if the list is empty
    def is_empty(self):
        return self.head is None

    # Method to insert an element at the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to insert an element at the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Method to delete the first occurrence of a value in the list
    def delete(self, value):
        if self.head is None:
            return  # List is empty, nothing to delete

        # If the value to delete is in the head node
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    # Method to search for a value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # Method to print all the elements in the list
    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # Method to get the length of the linked list
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Method to get the last element
    def get_last(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.value

    # Method to remove the last element
    def remove_last(self):
        if self.head is None:
            return None  # List is empty

        if self.head.next is None:
            self.head = None  # Only one element in the list
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None  # Remove the last node
