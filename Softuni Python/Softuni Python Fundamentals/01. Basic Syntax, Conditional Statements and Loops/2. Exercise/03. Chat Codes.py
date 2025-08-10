msgs = []

for _ in range(int(input())):
    number = int(input())
    msgs.append("Hello" if number == 88 else "How are you?" if number == 86 else "GREAT!" if number < 88 else "Bye.")

print("\n".join(msgs))