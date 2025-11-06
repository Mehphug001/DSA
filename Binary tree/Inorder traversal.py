class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Creating tree nodes
drink = Node("Drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

# Building the binary tree structure
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta
drink.left = hot
drink.right = cold


def Inorder(node):#[left->root->right]
    if node == None:
        return
    Inorder(node.left)
    print(node.val)
    Inorder(node.right)

Inorder(drink)


'''
        Drinks
         /   \
       hot    cold
      /  \    /   \
    tea coffee cola fanta
'''
