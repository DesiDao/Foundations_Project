class HashIndex:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Table with `size` number of empty lists (buckets)

    def _hash(self, key):
        """Generate a hash index for the key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert key-value pair into the hash index."""
        index = self._hash(key)
        # If key already exists, update the value
        for pair in self.table[index]:
            if pair[0] == key:
                pair = (key, value)
                return
        # If key doesn't exist, add a new pair to the corresponding bucket
        self.table[index].append((key, value))

    def delete(self, key):
        """Delete key-value pair from the hash index."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True  # Key was found and deleted
        return False  # Key was not found

    def search(self, key):
        """Search for a value by key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return value associated with key
        return None  # Key not found
