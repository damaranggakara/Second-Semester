#inisialisasi tree
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

#membuat penggambaran
def print_tree(root, level=0, prefix="", is_left=None):
    if root is not None:
        print_tree(root.right, level + 1, "   ", False)
        if level == 0:
            print(f"Root: {root.val}")
        else:
            print(prefix + ("|--" if is_left else "\\--") + str(root.val))
        print_tree(root.left, level + 1, prefix + ("|  " if is_left else "   "), True)

#insert bst
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left =TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(10)
root.right.right.left = TreeNode(11)
root.right.right.right = TreeNode(12)
root.right.right.left.left= TreeNode(13)
root.right.right.right.left = TreeNode(14)


#print bst
print_tree(root)