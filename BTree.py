class BTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BTreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BTreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def get_height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_distance_from_root(self, key):
        return self._get_distance_from_root(self.root, key, 0)

    def _get_distance_from_root(self, node, key, distance):
        if node is None:
            return -1  # Key not found
        if node.key == key:
            return distance
        elif key < node.key:
            return self._get_distance_from_root(node.left, key, distance + 1)
        else:
            return self._get_distance_from_root(node.right, key, distance + 1)

    def is_balanced(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return True
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return abs(left_height - right_height) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right)
