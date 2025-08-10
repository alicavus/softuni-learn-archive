parantheses = { "}" : "{",  "]": "[", ")" : "("}
stack = []

balanced = True

for p in input():
    if p in "{([":
        stack.append(p)
    elif p in "})]":
        if stack:
            if parantheses[p] != stack[-1]:
                balanced = False
                break
            stack.pop()
        else:
            balanced = False
            break

if stack:
    balanced = False

print("YES" if balanced else "NO")
    