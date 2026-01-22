from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create nodes
n1 = Node(5)
n2 = Node(3)
n3 = Node(1)
n4 = Node(6)
n5 = Node(2)
n6 = Node(7)
n7 = Node(8)

# Build the tree:
#               5
#             /   \
#            3     1
#          /  \    / \
#         6   2   8   7

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7


def TopView(root):
    if not root:
        return []

    ans = []
    queue = deque()
    result = {}

    queue.append((root, 0))  # (node, horizontal_distance)

    while queue:
        e, line = queue.popleft()

        # Only record first node seen at each horizontal distance
        if line not in result:
            result[line] = e.val

        if e.left:
            queue.append((e.left, line - 1))
        if e.right:
            queue.append((e.right, line + 1))

    # After BFS, sort by horizontal distance and collect values
    for key in sorted(result.keys()):
        ans.append(result[key])

    return ans


print("Top View:", TopView(n1))
