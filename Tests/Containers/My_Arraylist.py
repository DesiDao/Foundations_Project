import unittest

class TestArrayList(unittest.TestCase):
    def setUp(self):
        """Initialize a test list before each test."""
        self.array_list = ArrayList()
        self.array_list.append(1)
        self.array_list.append(2)
        self.array_list.append(3)

    def test_append(self):
        self.array_list.append(4)
        self.assertEqual(self.array_list.get(3), 4)
    
    def test_clear(self):
        self.array_list.clear()
        self.assertEqual(self.array_list.size(), 0)
    
    def test_copy(self):
        copied = self.array_list.copy()
        self.assertEqual(copied.size(), self.array_list.size())
    
    def test_remove(self):
        self.array_list.remove(2)
        with self.assertRaises(ValueError):
            self.array_list.get(2)
    
    def test_reverse(self):
        self.array_list.reverse()
        self.assertEqual(self.array_list.get(0), 3)
    
    def test_sort(self):
        self.array_list.append(0)
        self.array_list.sort()
        self.assertEqual(self.array_list.get(0), 0)
    
    def test_get_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array_list.get(5)
    
    def test_size(self):
        self.assertEqual(self.array_list.size(), 3)

if __name__ == "__main__":
    unittest.main()

