class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "can't pop, the stack is empty."
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return "can't top, stack is empty."
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(f"stack content={stack.items}")
print(f"popped item={stack.pop()}")
print(f"stack content={stack.items}")
print(f"top item after pop={stack.top()}")
print(f"stack is empty={stack.is_empty()}")
