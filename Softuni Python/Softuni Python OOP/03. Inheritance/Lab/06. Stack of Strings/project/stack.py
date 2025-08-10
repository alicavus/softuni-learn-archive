
class EmptyStackError(Exception):
    '''Raised when stack is empty'''
    pass


class Stack:
    def __init__(self):
        self.data: list[str] = []
    
    def push(self, element: str) -> str:
        self.data += [element]
        return element
    
    def pop(self) -> str:
        if not self.data:
            raise EmptyStackError("Cannot remove element from empty Stack")
        return self.data.pop()
    
    def top(self) -> str:
        if not self.data:
            raise EmptyStackError("Cannot get top element of empty stack")
        return self.data[-1]
    
    def is_empty(self) -> bool:
        return len(self.data) == 0
    
    def __str__(self) -> str:
        return "[" + ", ".join(self.data[::-1]) + "]"
            
