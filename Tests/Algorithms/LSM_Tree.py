# Example Usage
if __name__ == "__main__":
    lsm = LSMTree(memtable_threshold=3)
    lsm.insert(1, "A")
    lsm.insert(2, "B")
    lsm.insert(3, "C")  # This will trigger a flush
    lsm.insert(4, "D")
    
    print(lsm.lookup(1))  # Should print "A"
    print(lsm.range_query(1, 3))  # Should print {1: 'A', 2: 'B', 3: 'C'}

class TestLSMTree(unittest.TestCase):
    def setUp(self):
        self.lsm = LSMTree(memtable_threshold=3, sstable_file='test_sstable.pkl')
        if os.path.exists('test_sstable.pkl'):
            os.remove('test_sstable.pkl')
    
    def tearDown(self):
        if os.path.exists('test_sstable.pkl'):
            os.remove('test_sstable.pkl')
    
    def test_insert_and_lookup(self):
        self.lsm.insert(10, "X")
        self.assertEqual(self.lsm.lookup(10), "X")
    
    def test_flush_and_lookup(self):
        self.lsm.insert(1, "A")
        self.lsm.insert(2, "B")
        self.lsm.insert(3, "C")  # Triggers flush
        self.lsm.insert(4, "D")
        
        self.assertEqual(self.lsm.lookup(1), "A")
        self.assertEqual(self.lsm.lookup(4), "D")
    
    def test_range_query(self):
        self.lsm.insert(1, "A")
        self.lsm.insert(2, "B")
        self.lsm.insert(3, "C")  # Flush occurs
        self.lsm.insert(4, "D")
        
        result = self.lsm.range_query(1, 3)
        self.assertEqual(result, {1: "A", 2: "B", 3: "C"})
    
if __name__ == "__main__":
    unittest.main()
