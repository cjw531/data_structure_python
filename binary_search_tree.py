class BSTNode:
    def __init__ (self, key, value):
        # key might be omitted and compared with value only
        self.key = key 
        self.value = value
        self.left = None
        self.right = None

# O(height)
def search (root, key):
    if (root == None or key == root.key):
        return root
    elif (compare(root.key, key)):
        return search(root.left, key)
    elif (not compare(root.key, key)):
        return search(root.right, key)

# O(height)
def insert (root, new_node):
    if (root == None):
        root = new_node
    elif (root.key == new_node.key): # key exists already
        root.value = new_node.value # override value (BST x allow duplicate)
    elif (compare(root.key, new_node.key)): # left
        if (root.left == None):
            root.left = new_node
        else:
            insert(root.left, new_node)
    elif (not compare(root.key, new_node.key)): # right
        if (root.right == None):
            root.right = new_node
        else: 
            insert(root.right, new_node)

def remove (root, key, parent):
    if (root == None):
        print ("Unable to delete: Key does not exist")
    elif (root.key == key): # found node
        # no children (leaf node)
        if (root.left == None and root.right == None):
            if (parent != None):
                parent.left = None
                parent.right = None
            root.key = None
            root.value = None
            root = None

        # left child exists
        elif (not (root.left == None) and root.right == None):
            if (parent == None):
                root.key = root.left.key
                root.value = root.left.value
                root.left = root.left.left
                root.right = root.left.right
            elif (parent.left == root):
                parent.left = root.left
            elif (parent.right == root):
                parent.right = root.left
        
        # right child exists
        elif (root.left == None and not (root.right == None)):
            if (parent == None):
                root.key = root.right.key
                root.value = root.right.value
                root.left = root.right.left
                root.right = root.right.right
            elif (parent.left.key == root.key):
                parent.left = root.right
            elif (parent.right.key == root.key):
                parent.right = root.right

        # both children exists
        else:
            swap = min_node(root)
            if (parent == None):
                root.key = swap.key
                root.value = swap.value
                remove(root.right, swap.key, None)
            elif (parent.left.key == root.key):
                parent.left = swap
            elif (parent.right.key == root.key):
                parent.right = swap

    elif (compare(root.key, key)): # left traverse
        remove(root.left, key, root)
    elif (not compare(root.key, key)): # right traverse
        remove(root.right, key, root)

# helper function for comparing key value
def compare (v1, v2):
    if (v1 > v2):
        return True
    return False

def min_node (root):
    current = root
    while (current.left != None):
        current = current.left

    return current

if __name__ == '__main__':
    print ("Current BST Structure:")
    print ("            44")
    print ("        /       \\")
    print ("      17         88")
    print ("     /  \\       /  \\")
    print ("    8   32     65   97")
    print ("                \\")
    print ("                 82")
    print ("                 /")
    print ("                76")

    # root
    root = BSTNode(44, "Fourty Four")

    # Left Subtree
    root.left = BSTNode(17, "Seventeen")
    root.left.left = BSTNode(8, "Eight")
    root.left.right = BSTNode(32, "Thirty Two")

    # Right Subtree
    root.right = BSTNode(88, "Eighty Eight")
    root.right.left = BSTNode(65, "Sixty Five")
    root.right.left.right = BSTNode(82, "Eighty Two")
    root.right.left.right.left = BSTNode(76, "Seventy Six")
    root.right.right = BSTNode(97, "Ninety Seven")
    
    # search()
    result = search(root, 65)
    print ("Testing successful search result (key, value):", "(", result.key, ",", result.value, ")")
    result = search(root, 68)
    print ("Testing unsuccessful search result (key, value):", result)

    # insert()
    new_node = BSTNode(65, "New Sixty Five")
    insert(root, new_node)
    result_pos = root.right.left
    print ("Testing existing key insertion result (key, value):", "(", result_pos.key, ",", result_pos.value, ")")
    new_node = BSTNode(68, "New Sixty Eight")
    insert(root, new_node)
    result_pos = root.right.left.right.left.left
    print ("Testing existing key insertion result (key, value):", "(", result_pos.key, ",", result_pos.value, ")")
    new_node = BSTNode(35, "New Thirty Five")
    insert(root, new_node)
    result_pos = root.left.right.right
    print ("Testing existing key insertion result (key, value):", "(", result_pos.key, ",", result_pos.value, ")")

    print ("After 2 insertions, current BST structure:")
    print ("            44")
    print ("        /       \\")
    print ("      17         88")
    print ("     /  \\       /  \\")
    print ("    8   32     65   97")
    print ("          \     \\")
    print ("          35     82")
    print ("                 /")
    print ("                76")
    print ("                /")
    print ("               68")

    # remove
    print ("Testing delete non-existing key:")
    remove(root, 70, None)

    remove(root, 35, None)
    result_pos = root.left.right.right
    print ("Testing removing a leaf node, deleted position:", result_pos)

    print ("After removing a leaf node, current BST structure:")
    print ("            44")
    print ("        /       \\")
    print ("      17         88")
    print ("     /  \\       /  \\")
    print ("    8   32     65   97")
    print ("                \\")
    print ("                 82")
    print ("                 /")
    print ("                76")
    print ("                /")
    print ("               68")

    remove(root, 65, None)
    result_pos = root.right.left
    print ("Testing removing a node with its right child (k, v):", "(", result_pos.key, ",", result_pos.value, ")")

    print ("After removing a node with its right child, current BST structure:")
    print ("            44")
    print ("        /       \\")
    print ("      17         88")
    print ("     /  \\       /  \\")
    print ("    8   32     82   97")
    print ("               /")
    print ("              76")
    print ("             /")
    print ("            68")

    remove(root, 82, None)
    result_pos = root.right.left
    print ("Testing removing a node with its left child (k, v):", "(", result_pos.key, ",", result_pos.value, ")")

    print ("After removing a node with its left child, current BST structure:")
    print ("            44")
    print ("        /       \\")
    print ("      17         88")
    print ("     /  \\       /  \\")
    print ("    8   32     76   97")
    print ("               /")
    print ("              68")

    remove(root, 44, None)
    result_pos = root
    print ("Testing removing a node with both children (k, v):", "(", result_pos.key, ",", result_pos.value, ")")

    print ("After removing a node with both children, current BST structure:")
    print ("            8")
    print ("        /       \\")
    print ("      17         88")
    print ("        \\       /  \\")
    print ("        32     76   97")
    print ("               /")
    print ("              68")

    new_root = BSTNode(5, "Five")
    new_root.left = BSTNode(17, "Seventeen")
    new_root.left.left = BSTNode(30, "Thirty")
    result_pos = new_root
    remove(new_root, 5, None)
    print ("Testing removing root with left children (k, v):", "(", result_pos.key, ",", result_pos.value, ")")
    print ("Left, Right of NEW root:", new_root.left.key, new_root.right)