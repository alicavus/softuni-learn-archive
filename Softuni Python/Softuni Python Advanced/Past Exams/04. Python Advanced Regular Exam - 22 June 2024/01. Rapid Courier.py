from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])

delivered = 0

while packages and couriers:
    curr_package = packages.pop()
    curr_courier = couriers.popleft()

    if curr_courier >= curr_package:
        delivered += curr_package
        curr_courier -= 2 * curr_package

        if curr_courier > 0:
            couriers.append(curr_courier)
    
    else:
        delivered += curr_courier
        curr_package -= curr_courier
        packages.append(curr_package)

print(f"Total weight: {delivered} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")

else:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")


