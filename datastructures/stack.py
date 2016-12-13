class Stack:
    def __init__(self):
        self.data = []
    def push(self, elem):
        self.data.append(elem)
    def __len__(self):
        return len(self)
    def empty(self):
        return len(self)==0
    def pop(self):
        self.data.pop()
    def peek(self):
        return self.data[0]

