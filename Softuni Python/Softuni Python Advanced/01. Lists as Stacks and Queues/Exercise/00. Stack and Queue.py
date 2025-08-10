from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def top(self):
        if self.container:
            return self.container[0]
        raise ValueError
    
    def push(self, value):
        self.container.appendleft(value)
    
    def pop(self):
        if self.container:
            return self.container.popleft()
        raise ValueError

class Queue:
    def __init__(self):
        self.container = deque()

    def front(self):
        if self.container:
            return self.container[len(self.container) - 1]
        raise ValueError

    def back(self):
        if self.container:
            return self.container[0]
        raise ValueError
    
    def push_front(self, value):
        self.container.append(value)
    
    def push_back(self, value):
        self.container.appendleft(value)
    
    def pop_front(self):
        if self.container:
            return self.container.pop()
        raise ValueError
    
    def pop_back(self):
        if self.container:
            return self.container.popleft()
        raise ValueError