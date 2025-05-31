#inisialisasi tree
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

#membuat penggambaran
def print_tree(root, level=0, prefix="", is_left=None):
    if root is not None:
        print_tree(root.right, level + 1, "      ", False)
        if level == 0:
            print(f"Root: {root.val}")
        else:
            print(prefix + ("|--" if is_left else "\\--") + str(root.val))
        print_tree(root.left, level + 1, prefix + ("|     " if is_left else "      "), True)

#insert bst
root = TreeNode(80)
root.left = TreeNode(75)
root.right = TreeNode(85)
root.left.left = TreeNode(72)
root.left.right = TreeNode(77)
root.right.left = TreeNode(82)
root.right.right = TreeNode(87)
root.left.left.left = TreeNode(70)
root.left.left.right = TreeNode(78)
root.right.left.left = TreeNode(81)
root.left.right.right = TreeNode(90)

#print bst
print_tree(root)

