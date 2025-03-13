import bisect
import os
import pickle
from collections import OrderedDict
import unittest

class MemTable:
    def __init__(self, threshold=5):
        self.threshold = threshold
        self.table = OrderedDict()
    
    def insert(self, key, value):
        self.table[key] = value
        if len(self.table) >= self.threshold:
            return True  # Signal to flush
        return False
    
    def lookup(self, key):
        return self.table.get(key, None)
    
    def range_query(self, start, end):
        return {k: self.table[k] for k in self.table if start <= k <= end}
    
    def flush(self):
        sorted_items = sorted(self.table.items())
        self.table.clear()
        return sorted_items

class SSTable:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)
    
    def read(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'rb') as f:
            return pickle.load(f)
    
    def lookup(self, key):
        data = self.read()
        idx = bisect.bisect_left(data, (key,))
        if idx < len(data) and data[idx][0] == key:
            return data[idx][1]
        return None
    
    def range_query(self, start, end):
        data = self.read()
        return {k: v for k, v in data if start <= k <= end}

class LSMTree:
    def __init__(self, memtable_threshold=5, sstable_file='sstable.pkl'):
        self.memtable = MemTable(memtable_threshold)
        self.sstable = SSTable(sstable_file)
    
    def insert(self, key, value):
        if self.memtable.insert(key, value):
            self.flush()
    
    def lookup(self, key):
        value = self.memtable.lookup(key)
        if value is not None:
            return value
        return self.sstable.lookup(key)
    
    def range_query(self, start, end):
        results = self.sstable.range_query(start, end)
        results.update(self.memtable.range_query(start, end))
        return dict(sorted(results.items()))
    
    def flush(self):
        memtable_data = self.memtable.flush()
        sstable_data = self.sstable.read()
        merged_data = sorted(set(sstable_data + memtable_data))
        self.sstable.write(merged_data)
