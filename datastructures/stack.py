class Stack:
    def __init__(self):
        pass
    def push(self, elem):
        raise NotImplementedError
    def __len__(self):
        return 0
    def empty(self):
        return len(self)==0
    def pop(self):
        raise IndexError
    def peep(self):
        raise IndexError
