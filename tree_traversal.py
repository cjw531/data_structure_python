class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

# global variable to append result:
result = []

# O(n) to traverse tree
# root-left-right
def pre_order (root):
    if (root != None):
        result.append(root.value)
        pre_order (root.left)
        pre_order (root.right)

# left-root-right
def in_order (root):
    if (root != None):
        in_order (root.left)
        result.append(root.value)
        in_order (root.right)

# left-right-root
def post_order (root):
    if (root != None):
        post_order (root.left)
        post_order (root.right)
        result.append(root.value)

# print helper function
def print_helper (root):
    global result
    result = []
    pre_order(root)
    print ("Pre-Order Sequence:", result)

    result = []
    in_order(root)
    print ("In-Order Sequence:", result)

    result = []
    post_order(root)
    print ("Post-Order Sequence:", result)

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
    print_helper(root)
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
    print_helper(root)
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
    print_helper(root)