from stack import *

class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

"""
we do two calls, each on one half of the tree
T(n) = 2 * T(n/2) + 1 = O(n)
       ^-a     ^-b  ^-f(n)
"""
# assume that the given tree has at least 1 node (root)
def depth_recursive (root):
    if (root == None):
        return -1
    
    left = depth_recursive(root.left)
    right = depth_recursive(root.right)

    return (1 + max(left, right))

def depth_stack (root):
    result = -1
    s = Stack()
    s.push (tuple([root, -1]))

    while (not s.is_empty()):
        top = s.top()[0]
        depth = s.top()[1]
        s.pop()

        if (top == None):
            result = max(result, depth)
        else:
            s.push(tuple([top.left, depth + 1]))
            s.push(tuple([top.right, depth + 1]))
    
    return result

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
    print ("Maximum depth with recursive approach:", depth_recursive(root))
    print ("Maximum depth with stack approach:", depth_stack(root))
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
    print ("Maximum depth with recursive approach:", depth_recursive(root))
    print ("Maximum depth with stack approach:", depth_stack(root))
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
    print ("Maximum depth with recursive approach:", depth_recursive(root))
    print ("Maximum depth with stack approach:", depth_stack(root))
    


    