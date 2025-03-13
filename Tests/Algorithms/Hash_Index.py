import unittest

class TestHashIndex(unittest.TestCase):
    
    def setUp(self):
        """Set up a hash index before each test."""
        self.hash_index = HashIndex(size=5)  # Small size for controlled testing
        self.hash_index.insert("apple", 10)
        self.hash_index.insert("banana", 20)
        self.hash_index.insert("cherry", 30)

    def test_insert(self):
        """Test that inserted elements exist in the hash table."""
        self.hash_index.insert("date", 40)
        self.assertEqual(self.hash_index.search("date"), 40)
    
    def test_search_existing(self):
        """Test searching for an existing key."""
        self.assertEqual(self.hash_index.search("banana"), 20)

    def test_search_non_existing(self):
        """Test searching for a non-existing key."""
        self.assertIsNone(self.hash_index.search("orange"))
    
    def test_delete_existing(self):
        """Test deleting an existing key."""
        self.assertTrue(self.hash_index.delete("cherry"))
        self.assertIsNone(self.hash_index.search("cherry"))

    def test_delete_non_existing(self):
        """Test deleting a non-existing key."""
        self.assertFalse(self.hash_index.delete("grape"))

    def test_size(self):
        """Test that the size function correctly counts elements."""
        self.assertEqual(self.hash_index.get_size(), 3)
        self.hash_index.insert("date", 40)
        self.assertEqual(self.hash_index.get_size(), 4)
        self.hash_index.delete("apple")
        self.assertEqual(self.hash_index.get_size(), 3)

    def test_distance(self):
        """Test that distance function returns the correct bucket index."""
        index_apple = self.hash_index.distance("apple")
        index_banana = self.hash_index.distance("banana")
        self.assertIsInstance(index_apple, int)
        self.assertIsInstance(index_banana, int)
        self.assertGreaterEqual(index_apple, 0)
        self.assertGreaterEqual(index_banana, 0)
        self.assertLess(index_apple, self.hash_index.size)
        self.assertLess(index_banana, self.hash_index.size)

    def test_collision_handling(self):
        """Test that multiple values in the same bucket can exist."""
        # Force a collision by inserting a key that hashes to an existing bucket
        key1 = "apple"
        key2 = "elderberry"  # Assuming it hashes to the same bucket as "apple"
        self.hash_index.insert(key2, 50)
        
        bucket_index = self.hash_index._hash(key1)
        bucket_contents = self.hash_index.table[bucket_index]
        
        keys_in_bucket = {pair[0] for pair in bucket_contents}
        self.assertIn("apple", keys_in_bucket)
        self.assertIn("elderberry", keys_in_bucket)

if __name__ == '__main__':
    unittest.main()

