class AVLNode:
    def __init__ (self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0

class AVLTree:
    def insert (self, root, new_node):
        if (root == None):
            root = new_node
        elif (root.value == new_node.value): # key value exists already
            root.value = new_node.value
        elif (root.value > new_node.value): # left
            root.left = self.insert(root.left, new_node)
        elif (root.value <= new_node.value): # right
            root.right = self.insert(root.right, new_node)
        
        root.bf = self.balance_factor(root)

        # Left Left 
        if (root.bf > 1 and new_node.value < root.left.value): 
            return self.right_rotate(root) 
    
        # Right Right 
        if (root.bf < -1 and new_node.value > root.right.value): 
            return self.left_rotate(root) 

        # Left Right 
        if (root.bf > 1 and new_node.value > root.left.value): 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root) 

        # Right Left 
        if (root.bf < -1 and new_node.value < root.right.value): 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root)

        return root

    def remove (self, root, key):
        if not root: 
            return root 
  
        elif key < root.value: 
            root.left = self.remove(root.left, key) 
  
        elif key > root.value: 
            root.right = self.remove(root.right, key) 
  
        else: # ==
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.min_node(root.right) 
            root.val = temp.value
            root.right = self.remove(root.right, temp.value) 

        if root is None: 
            return root 

        root.bf = self.balance_factor(root)
        root.left.bf = self.balance_factor(root.left)
        root.right.bf = self.balance_factor(root.right)

        # Left Left 
        if (root.bf > 1 and root.left.bf >= 0): 
            return self.right_rotate(root) 
    
        # Right Right 
        if (root.bf < -1 and root.right.bf <= 0): 
            return self.left_rotate(root) 

        # Left Right 
        if (root.bf > 1 and root.left.bf < 0): 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root) 

        # Right Left 
        if (root.bf < -1 and root.right.bf > 0): 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root)

        return root

    def left_rotate (self, z):
        y = z.right 
        T2 = y.left 

        y.left = z 
        z.right = T2

        self.post_order_traverse(y)
        return y

    def right_rotate (self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self.post_order_traverse(y)
        return y

    def balance_factor (self, node):
        if not node:
            return 0

        left_subtree = self.height(node.left)
        right_subtree = self.height(node.right)

        return (left_subtree - right_subtree)

    # O(n)
    def height (self, node):
        if (node == None):
            return 0

        left = self.height (node.left)
        right = self.height (node.right)

        return 1 + max(left, right)

    # travel the whole tree -> update balance factor
    def post_order_traverse (self, node):
        if (node != None):
            self.post_order_traverse(node.left)
            self.post_order_traverse(node.right)
            node.bf = self.balance_factor(node)

    def min_node (self, root):
        current = root
        while (current.left != None):
            current = current.left

        return current

    result = []
    def pre_order (self, root):
        if (root != None):
            result.append(root.value)
            self.pre_order (root.left)
            self.pre_order (root.right)

    # print helper function
    def print_helper (self, root):
        global result
        result = []
        self.pre_order(root)
        print ("Pre-Order Sequence:", result)

if __name__ == '__main__':
    avl = AVLTree()
    root = None
    root = avl.insert(root, AVLNode(10)) 
    root = avl.insert(root, AVLNode(20)) 
    root = avl.insert(root, AVLNode(30)) 
    root = avl.insert(root, AVLNode(40)) 
    root = avl.insert(root, AVLNode(50)) 
    root = avl.insert(root, AVLNode(25)) 

    print (root.value, root.bf)
    print (root.left.value, root.left.bf)
    print (root.right.value, root.right.bf)
    # ==
    r = None
    tree_elem = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
    avl2 = AVLTree()
    for i in tree_elem: 
        r = avl2.insert(r, AVLNode(i))
    
    print (r.value, r.bf)
    print (r.left.value, r.left.bf)
    print (r.right.value, r.right.bf)

    avl2.print_helper(r)
    r = avl2.remove(r, 10)
    avl2.print_helper(r)

    print (r.value, r.bf)
    print (r.left.value, r.left.bf)
    print (r.right.value, r.right.bf)