class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create nodes
n1  = Node(3)
n2  = Node(3)
n3  = Node(1)
n4  = Node(1)
n5  = Node(2)
n6  = Node(3)
n7  = Node(6)
n8  = Node(1)
n9  = Node(2)
n10 = Node(1)

# Build the tree exactly:
#               3
#             /   \
#            3     1
#          /  \   / \
#         1    2 3   6
#        / \
#       1   2
#      /
#     1
n1.left  = n2
n1.right = n3

n2.left  = n4
n2.right = n5

n3.left  = n6
n3.right = n7

n4.left  = n8
n4.right = n9

n8.left  = n10

# ✅ Function to check if tree is balanced:
def solve(node):
    if node is None:
        return 0  # Height of empty tree is 0

    lh = solve(node.left)
    if lh == -1:
        return -1  # Left subtree unbalanced

    rh = solve(node.right)
    if rh == -1:
        return -1  # Right subtree unbalanced

    if abs(lh - rh) > 1:
        return -1  # Current node unbalanced

    return 1 + max(lh, rh)  # Return height

# ✅ Final check
def isBalanced(root):
    return solve(root) != -1

# ✅ Output
print(isBalanced(n1))  # This will print True or False
