class String:
    def __init__(self, value: str):
        # Manually create an internal array-like structure to hold characters
        self._length = len(value)
        self._value = self._create_char_array(value)
    
    def _create_char_array(self, value: str):
        # Manually create a character array (as a list of characters)
        array = []
        for ch in value:
            array.append(ch)
        return array

    def length(self):
        # Return the length of the string
        return self._length
    
    def concat(self, other):
        # Concatenate the current string with another String object
        if isinstance(other, String):
            for ch in other._value:
                self._value.append(ch)
            self._length += other.length()
        elif isinstance(other, str):
            for ch in other:
                self._value.append(ch)
            self._length += len(other)
        return self

    def __str__(self):
        # Convert internal array of characters to a string
        return ''.join(self._value)
    
    def equals(self, other):
        # Compare two strings for equality
        if isinstance(other, String):
            if self._length != other.length():
                return False
            for i in range(self._length):
                if self._value[i] != other._value[i]:
                    return False
            return True
        elif isinstance(other, str):
            if self._length != len(other):
                return False
            for i in range(self._length):
                if self._value[i] != other[i]:
                    return False
            return True
        return False
    
    def to_upper(self):
        # Convert all characters to uppercase
        for i in range(self._length):
            self._value[i] = self._value[i].upper()
        return self
    
    def to_lower(self):
        # Convert all characters to lowercase
        for i in range(self._length):
            self._value[i] = self._value[i].lower()
        return self
    
    def char_at(self, index):
        # Return character at a specific index
        if 0 <= index < self._length:
            return self._value[index]
        raise IndexError("Index out of range.")
    
    def substring(self, start, end):
        # Return a substring from start to end (exclusive)
        if 0 <= start < self._length and 0 <= end <= self._length:
            sub_str = ''.join(self._value[start:end])
            return String(sub_str)
        raise IndexError("Index out of range.")
    
    def compare_to(self, other):
        # Compare two strings lexicographically
        if isinstance(other, String):
            for i in range(min(self._length, other.length())):
                if self._value[i] < other._value[i]:
                    return -1
                elif self._value[i] > other._value[i]:
                    return 1
            if self._length < other.length():
                return -1
            elif self._length > other.length():
                return 1
            return 0
        elif isinstance(other, str):
            for i in range(min(self._length, len(other))):
                if self._value[i] < other[i]:
                    return -1
                elif self._value[i] > other[i]:
                    return 1
            if self._length < len(other):
                return -1
            elif self._length > len(other):
                return 1
            return 0
        return False
