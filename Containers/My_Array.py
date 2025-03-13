class My_Array:
    def __init__(self, *args):
        """Initialize the array with optional values."""
        self.data = list(args)
    
    def append(self, value):
        """Append a value to the array."""
        self.data.append(value)
    
    def remove(self, value):
        """Remove first occurrence of value from the array."""
        if value in self.data:
            self.data.remove(value)
        else:
            raise ValueError("Value not found in array.")
    
    def get(self, index):
        """Get value at a specific index."""
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range.")
    
    def size(self):
        """Return the size of the array."""
        return len(self.data)
    
    def __repr__(self):
        """String representation of the array."""
        return f"CustomArray({self.data})"
