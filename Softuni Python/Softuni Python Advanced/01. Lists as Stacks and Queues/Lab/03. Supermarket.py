from collections import deque

queue = deque()

while True:
    customer = input()
    if customer.lower() == "end":
        print(f"{len(queue)} people remaining.")
        break
    elif customer.lower() == "paid":
        print("\n".join(queue))
        queue.clear()
    else:
        queue.append(customer)
