import unittest

class TestBTree(unittest.TestCase):
    def setUp(self):
        self.btree = BTree()
        self.values = [50, 30, 70, 20, 40, 60, 80]
        for v in self.values:
            self.btree.insert(v)

    def test_insertion_and_traversal(self):
        expected_traversal = sorted(self.values)
        self.assertEqual(self.btree.inorder_traversal(), expected_traversal)

    def test_search(self):
        self.assertIsNotNone(self.btree.search(30))
        self.assertIsNone(self.btree.search(100))

    def test_height(self):
        self.assertEqual(self.btree.get_height(), 2)

    def test_distance_from_root(self):
        self.assertEqual(self.btree.get_distance_from_root(50), 0)
        self.assertEqual(self.btree.get_distance_from_root(30), 1)
        self.assertEqual(self.btree.get_distance_from_root(20), 2)
        self.assertEqual(self.btree.get_distance_from_root(100), -1)  # Not in tree

    def test_is_balanced(self):
        self.assertTrue(self.btree.is_balanced())

if __name__ == "__main__":
    unittest.main()
