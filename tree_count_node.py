class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

def node_count_recursive(node): 
    if node is None:
        return 0
    return 1 + node_count_recursive(node.left) + node_count_recursive(node.right)

if __name__ == '__main__':
    print ("Input tree structure:")
    print ("       0")
    print ("     /   \\")
    print ("    1     2")
    print ("  /  \\")
    print (" 3    4")
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    print ("Count all nodes with recursive approach:", node_count_recursive(root))
    print ("==========================================")
    print ("Input tree structure:")
    print ("       0")
    print ("     /   \\")
    print ("    1     2")
    print ("           \\")
    print ("            3")
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print ("Count all nodes with recursive approach:", node_count_recursive(root))
    print ("==========================================")
    print ("Input tree structure:")
    print ("        1")
    print ("     /    \\")
    print ("    2       3")
    print ("   /     /     \\")
    print ("  4     5       6")
    print ("         \\     /")
    print ("          7   8")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(8)
    root.right.left.right = TreeNode(7)
    print ("Count all nodes with recursive approach:", node_count_recursive(root))