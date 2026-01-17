# Global variable to store diameter
diameter = 0

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# Build the tree
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n6.left = n8
n8.left = n9

"""
Tree Structure:

              1
            /   \
           2     3
         /  \   / \
        4    5 6   7
                /
               8
              /
             9
"""

# Function to compute height and update diameter
def solve(node):
    global diameter
    if node is None:
        return 0

    left_height = solve(node.left)
    right_height = solve(node.right)

    # Update diameter = max of current diameter OR path through this node
    diameter = max(diameter, left_height + right_height)

    return 1 + max(left_height, right_height)

# Call function
solve(n1)
print("Diameter of the tree:", diameter)
