from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

bullets_left = min(len(bullets), gun_barrel_size)

expences = 0

while True:
    if not bullets_left:
        if bullets:
            print("Reloading!")
            bullets_left = min(len(bullets), gun_barrel_size)

    if not locks:
        money_earned = value - expences
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break
    
    elif not bullets:
        locks_left = len(locks)
        print(f"Couldn't get through. Locks left: {locks_left}")
        break

    curr_bullet = bullets.pop()
    curr_lock = locks.popleft()
    expences += bullet_price
    bullets_left -= 1

    if curr_bullet > curr_lock:
        locks.appendleft(curr_lock)
        print("Ping!")
    
    else:
        print("Bang!")

    

    

