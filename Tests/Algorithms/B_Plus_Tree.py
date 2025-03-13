import unittest

class TestBPlusTree(unittest.TestCase):
    def setUp(self):
        self.tree = BPlusTree(order=4)
        for key in [10, 20, 5, 6, 12, 30, 7, 17]:
            self.tree.insert(key)

    def test_search(self):
        self.assertTrue(self.tree.search(10))
        self.assertFalse(self.tree.search(15))

    def test_range_query(self):
        self.assertEqual(self.tree.range_query(6, 17), [6, 7, 10, 12])
        self.assertEqual(self.tree.range_query(20, 30), [20, 30])

if __name__ == "__main__":
    unittest.main()
