from project.stack import Stack

s = Stack()
print(s.is_empty())

s.push("Test")
s.push("another")
s.push("more")
print(s.is_empty(), s.top(), s)