class Stack:

    def __init__(self, items=[], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            Exception("Limit exceeded")

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if len(self.items) >= self.limit else False

    def search(self, target):
        for index, item in enumerate(self.items[::-1]):
            if item == target:
                return index
        return -1
