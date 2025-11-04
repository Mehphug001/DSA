class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

drink=Node("Drinks")
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

hot.left=tea
hot.right=coffee
cold.left=cola
cold.right=fanta
drink.left=hot
drink.right=cold

print(drink.right.val)
print(drink.left.left.val)
print(hot.right.val)