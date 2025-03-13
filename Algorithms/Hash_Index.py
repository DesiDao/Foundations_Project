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

    
    def get_size(self):
        """Return the number of elements stored in the hash index."""
        size = 0
        for bucket in self.table:
            size += len(bucket)
        return size

    def distance(self, key):
        """Calculate the distance from the key's bucket index to the current location (bucket)."""
        index = self._hash(key)
        # Return the index of the bucket where the key should be
        return index

    def print_table(self):
        """Print out the hash table."""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")

# Example usage
hash_index = HashIndex(size=5)  # Create a hash table with 5 buckets

# Insert key-value pairs
hash_index.insert("apple", 10)
hash_index.insert("banana", 20)
hash_index.insert("cherry", 30)
hash_index.insert("date", 40)
hash_index.insert("elderberry", 50)

# Print the table
print("Hash Table:")
hash_index.print_table()

# Search for a key
print("\nSearch for 'banana':", hash_index.search("banana"))

# Delete a key
print("\nDelete 'cherry':", hash_index.delete("cherry"))

# Print the table after deletion
print("\nHash Table after deletion of 'cherry':")
hash_index.print_table()

# Get the size of the table
print("\nSize of hash table:", hash_index.get_size())

# Calculate the "distance" (bucket index) for a key
print("\nDistance for 'elderberry':", hash_index.distance("elderberry"))
