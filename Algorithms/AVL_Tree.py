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

    
    def _delete(self, node, key):
        # Perform standard BST delete
        if not node:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get the inorder successor
            temp = self._get_min_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        
        # Update height of the current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Get the balance factor
        balance = self._get_balance_factor(node)
        
        # Balance the node if it becomes unbalanced
        if balance > 1 and self._get_balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _distance_to_root(self, node, key, depth=0):
        if node is None:
            return -1  # Key not found
        if node.key == key:
            return depth
        elif key < node.key:
            return self._distance_to_root(node.left, key, depth + 1)
        else:
            return self._distance_to_root(node.right, key, depth + 1)

    def distance_to_root(self, key):
        return self._distance_to_root(self.root, key)

    def _print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            self._print_tree(node.left, level + 1, "L--- ")
            self._print_tree(node.right, level + 1, "R--- ")

    def print_tree(self):
        self._print_tree(self.root)

# Example usage
avl_tree = AVLTree()

# Insert elements
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(25)
avl_tree.insert(5)

# Print the AVL tree
avl_tree.print_tree()

# Get distance from a node to the root
print("\nDistance from node 25 to root:", avl_tree.distance_to_root(25))

# Delete a node
avl_tree.delete(25)

# Print the tree after deletion
avl_tree.print_tree()
