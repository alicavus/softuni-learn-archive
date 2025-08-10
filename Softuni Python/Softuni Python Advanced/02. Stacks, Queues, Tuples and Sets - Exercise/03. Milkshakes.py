from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milks = deque(map(int, input().split(", ")))

shakes = 0

while chocolates and milks:
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    while milks and milks[0] <= 0:
        milks.popleft()
        
    if not chocolates or not milks:
        break
    
    if chocolates[-1] == milks[0]:
        chocolates.pop()
        milks.popleft()
        shakes += 1
    else:
        
        chocolates[-1] -= 5
        milks.append(milks.popleft())
        
    if shakes == 5:
        break
    
if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
    
if chocolates:
    print("Chocolate:", ", ".join(map(str, chocolates)))
else:
    print("Chocolate: empty")
    
if milks:
    print("Milk:", ", ".join(map(str, milks)))
else:
    print("Milk: empty")