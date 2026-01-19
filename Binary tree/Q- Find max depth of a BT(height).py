from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Creating tree nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# Building the binary tree structure
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


""" Recursive function to find height of the tree
def solve(node):
    if node is None:
        return 0
    left_height = solve(node.left)
    right_height = solve(node.right)
    return 1 + max(left_height, right_height)

# Calling the function on root
print("Height of the tree:", solve(n1))
"""

# Iterative method to find height of the tree (Level Order Traversal - BFS)
def levelorder_height(node):
    if not node:
        return 0

    height = 0
    queue = deque([node])

    while queue:
        level_size = len(queue)
        height += 1

        for _ in range(level_size):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return height

print("Height of the tree:", levelorder_height(n1))


