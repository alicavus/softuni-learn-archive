resources = {}

while True:
    resource = input()

    if resource == "stop":
        for resource in resources:
            print(f'{resource} -> {resources[resource]}')
        break

    quantity = int(input())

    if resource not in resources:
        resources[resource] = 0
    
    resources[resource] += quantity


