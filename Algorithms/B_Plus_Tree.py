import bisect

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None  # Used for leaf node traversal

class BPlusTree:
    def __init__(self, order=3):
        self.root = BPlusTreeNode(leaf=True)
        self.order = order

    def search(self, key):
        node = self.root
        while not node.leaf:
            i = bisect.bisect_left(node.keys, key)
            node = node.children[i]
        
        if key in node.keys:
            return True
        return False

    def insert(self, key):
        root = self.root
        split_key, new_child = self._insert_recursive(root, key)
        if new_child:
            new_root = BPlusTreeNode()
            new_root.keys = [split_key]
            new_root.children = [root, new_child]
            self.root = new_root
