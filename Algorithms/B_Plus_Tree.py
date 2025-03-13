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

    
    def _insert_recursive(self, node, key):
        if node.leaf:
            bisect.insort(node.keys, key)
            if len(node.keys) >= self.order:
                return self._split_leaf(node)
            return None, None

        i = bisect.bisect_left(node.keys, key)
        split_key, new_child = self._insert_recursive(node.children[i], key)
        if new_child:
            node.keys.insert(i, split_key)
            node.children.insert(i + 1, new_child)
            if len(node.keys) >= self.order:
                return self._split_internal(node)
        return None, None

    def _split_leaf(self, node):
        mid = len(node.keys) // 2
        new_node = BPlusTreeNode(leaf=True)
        new_node.keys = node.keys[mid:]
        node.keys = node.keys[:mid]
        
        new_node.next = node.next
        node.next = new_node
        return new_node.keys[0], new_node

    def _split_internal(self, node):
        mid = len(node.keys) // 2
        new_node = BPlusTreeNode()
        new_node.keys = node.keys[mid + 1:]
        new_node.children = node.children[mid + 1:]
        node.keys = node.keys[:mid]
        node.children = node.children[:mid + 1]
        return node.keys[mid], new_node

    def range_query(self, low, high):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        
        result = []
        while node:
            for key in node.keys:
                if low <= key <= high:
                    result.append(key)
            node = node.next
        return result
