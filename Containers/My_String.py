class String:
    def __init__(self, value: str):
        # Initialize the string value
        self._value = list(value)  # Store string as a list of characters
    
    def length(self):
        # Return the length of the string
        return len(self._value)
    
    def concat(self, other):
        # Concatenate the current string with another String object
        if isinstance(other, String):
            self._value.extend(other._value)
        elif isinstance(other, str):
            self._value.extend(list(other))
        return self
    
    def __str__(self):
        # Return string representation
        return ''.join(self._value)
    
    def equals(self, other):
        # Compare two strings for equality
        if isinstance(other, String):
            return self._value == other._value
        elif isinstance(other, str):
            return self._value == list(other)
        return False
    
    def to_upper(self):
        # Convert all characters to uppercase
        self._value = [ch.upper() for ch in self._value]
        return self
    
    def to_lower(self):
        # Convert all characters to lowercase
        self._value = [ch.lower() for ch in self._value]
        return self
    
    def char_at(self, index):
        # Return character at a specific index
        if 0 <= index < self.length():
            return self._value[index]
        raise IndexError("Index out of range.")
    
    def substring(self, start, end):
        # Return a substring from start to end (exclusive)
        if 0 <= start < self.length() and 0 <= end <= self.length():
            return String(''.join(self._value[start:end]))
        raise IndexError("Index out of range.")
    
    def compare_to(self, other):
        # Compare two strings lexicographically
        if isinstance(other, String):
            return (''.join(self._value) > ''.join(other._value)) - (''.join(self._value) < ''.join(other._value))
        elif isinstance(other, str):
            return (''.join(self._value) > other) - (''.join(self._value) < other)
        return False

