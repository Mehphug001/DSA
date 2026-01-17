class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create nodes
n1  = Node(25)
n2  = Node(-40)
n3  = Node(50)
n4  = Node(10)
n5  = Node(20)
n6  = Node(100)
n7  = Node(70)

# Build the tree:
#               25
#             /   \
#           -40   50
#          /  \   / \
#         10   20 100  70

n1.left  = n2
n1.right = n3
n2.left  = n4
n2.right = n5
n3.left  = n6
n3.right = n7

# ✅ Maximum Path Sum Code
maxi = float("-inf")

def solve(node):
    global maxi
    if node is None:
        return 0

    left_sum = solve(node.left)
    right_sum = solve(node.right)

    # If negative, don't include that path
    if left_sum < 0:
        left_sum = 0
    if right_sum < 0:
        right_sum = 0

    # Update maxi with maximum path sum through current node
    maxi = max(maxi, node.val + left_sum + right_sum)

    # Return max sum of path going down (not turning both sides)
    return node.val + max(left_sum, right_sum)

# Call the function
solve(n1)
print("Maximum Path Sum:", maxi)
