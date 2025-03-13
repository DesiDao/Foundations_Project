class ArrayList:
    def __init__(self):
        """Initialize an empty array with manual management."""
        self.data = None
        self.capacity = 0
        self.count = 0
    
    def _resize(self, new_capacity):
        """Resize the array to a new capacity."""
        new_data = [None] * new_capacity
        for i in range(self.count):
            new_data[i] = self.data[i] if self.data else None
        self.data = new_data
        self.capacity = new_capacity
    
    def append(self, value):
        """Append a value to the array."""
        if self.count == self.capacity:
            self._resize(self.capacity * 2 if self.capacity > 0 else 1)
        self.data[self.count] = value
        self.count += 1
    
    def clear(self):
        """Removes all elements from the array."""
        self.data = None
        self.capacity = 0
        self.count = 0
    
    def copy(self):
        """Returns a copy of the array."""
        new_list = ArrayList()
        for i in range(self.count):
            new_list.append(self.data[i])
        return new_list
    
    def count(self, value):
        """Returns the number of occurrences of a value in the array."""
        return sum(1 for i in range(self.count) if self.data[i] == value)
    
    def extend(self, iterable):
        """Extend the array by appending elements from an iterable."""
        for item in iterable:
            self.append(item)
    
    def index(self, value):
        """Returns the index of the first occurrence of a value."""
        for i in range(self.count):
            if self.data[i] == value:
                return i
        raise ValueError("Value not found in array.")
    
    def insert(self, index, value):
        """Insert a value at a specified index."""
        if index < 0 or index > self.count:
            raise IndexError("Index out of range.")
        if self.count == self.capacity:
            self._resize(self.capacity * 2 if self.capacity > 0 else 1)
        for i in range(self.count, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.count += 1
    
    def pop(self, index=None):
        """Removes and returns the element at the specified index."""
        if index is None:
            index = self.count - 1
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range.")
        value = self.data[index]
        self.remove(value)
        return value
    
    def remove(self, value):
        """Remove first occurrence of value from the array."""
        for i in range(self.count):
            if self.data[i] == value:
                for j in range(i, self.count - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.count - 1] = None
                self.count -= 1
                return
        raise ValueError("Value not found in array.")
    
    def reverse(self):
        """Reverses the order of the array."""
        for i in range(self.count // 2):
            self.data[i], self.data[self.count - 1 - i] = self.data[self.count - 1 - i], self.data[i]
    
    def sort(self):
        """Sorts the array in ascending order."""
        for i in range(self.count):
            for j in range(i + 1, self.count):
                if self.data[i] > self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def get(self, index):
        """Get value at a specific index."""
        if 0 <= index < self.count:
            return self.data[index]
        else:
            raise IndexError("Index out of range.")
    
    def size(self):
        """Return the size of the array."""
        return self.count
    
    def __repr__(self):
        """String representation of the array."""
        return f"ArrayList({[self.data[i] for i in range(self.count)]})"
