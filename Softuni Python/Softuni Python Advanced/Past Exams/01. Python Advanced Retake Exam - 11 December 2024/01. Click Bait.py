from collections import deque

suggested_list = deque([int(x) for x in input().split()])
featured_list = [int(x) for x in input().split()]
target_engagement_value = int(input())

final_feed = deque()

while suggested_list and featured_list:
    first_element = suggested_list.popleft()
    second_element = featured_list.pop()

    max_element = max(first_element, second_element)
    min_element = min(first_element, second_element)
    remainder = max_element % min_element

    origin = suggested_list if first_element > second_element else featured_list

    final_feed.append(
        remainder if origin == featured_list else -remainder
    )

    if remainder == 0:
        continue

    origin.append(2 * remainder)


total_engagement_value = sum(final_feed)

print("Final Feed: ", end = "")
print(*final_feed, sep = ", ")

if total_engagement_value < target_engagement_value:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")
else:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")









