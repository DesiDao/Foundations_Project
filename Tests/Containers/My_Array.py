import unittest

class TestCustomArray(unittest.TestCase):
    def setUp(self):
        """Initialize a test array before each test."""
        self.array = CustomArray(1, 2, 3)

    def test_append(self):
        self.array.append(4)
        self.assertEqual(self.array.get(3), 4)

    def test_remove(self):
        self.array.remove(2)
        self.assertNotIn(2, self.array.data)

    def test_remove_nonexistent(self):
        with self.assertRaises(ValueError):
            self.array.remove(10)

    def test_get(self):
        self.assertEqual(self.array.get(1), 2)

    def test_get_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array.get(5)

    def test_size(self):
        self.assertEqual(self.array.size(), 3)

if __name__ == "__main__":
    unittest.main()
