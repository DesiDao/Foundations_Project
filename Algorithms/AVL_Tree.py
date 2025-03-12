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
