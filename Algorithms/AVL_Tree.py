class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initially, height of a node is 1
      
class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        # Return new root
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        # Return new root
        return y

    def _insert(self, node, key):
        if not node:
            return Node(key)
        
        # Perform normal BST insertion
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        # Update height of this ancestor node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Get the balance factor of this ancestor node
        balance = self._get_balance_factor(node)
        
        # Balance the node if it becomes unbalanced
        if balance > 1 and key < node.left.key:  # Left-Left Case
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:  # Right-Right Case
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:  # Left-Right Case
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:  # Right-Left Case
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _get_min_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_node(node.left)
