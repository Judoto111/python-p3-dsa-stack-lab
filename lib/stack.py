
class Stack:
    def __init__(self, items=None, max_size=None):
        
        self.items = items if items is not None else []
        self.max_size = max_size

    def push(self, item):
        
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise IndexError("Stack is full")
        self.items.append(item)

    def pop(self):
        
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def size(self):
        
        return len(self.items)

    def is_empty(self):
        
        return len(self.items) == 0

    def full(self):
        
        return self.max_size is not None and len(self.items) >= self.max_size

    def search(self, item):
        
        if item in self.items:
            return len(self.items) - 1 - self.items.index(item)
        else:
            return -1
