from collections import deque

# Input parsing
suggested_links = deque([int(link) for link in input().split(" ")])
featured_articles = [int(a) for a in input().split(" ")]
target_engagement_value = int(input())

# Initialize variables
final_feed = []

# Process until one collection is empty
while suggested_links and featured_articles:
    # Take one element from each sequence
    fifo_element = suggested_links.popleft()  # First element of FIFO
    lifo_element = featured_articles.pop()    # Last element of LIFO

    # Compare the two elements
    if fifo_element > lifo_element:
        greater, smaller, origin = fifo_element, lifo_element, "FIFO"
    elif lifo_element > fifo_element:
        greater, smaller, origin = lifo_element, fifo_element, "LIFO"
    else:
        # If equal, add 0 and continue
        final_feed.append(0)
        continue

    # Calculate the remainder
    remainder = greater % smaller

    # Add remainder with the appropriate sign to the final feed
    if origin == "FIFO":
        final_feed.append(-remainder)
    else:
        final_feed.append(remainder)

    # Double the remainder and return it to the original collection
    if remainder != 0:
        if origin == "FIFO":
            suggested_links.append(remainder * 2)  # Return to the end of FIFO
        else:
            featured_articles.append(remainder * 2)   # Return to the end of LIFO

# Calculate Total Engagement Value
total_engagement_value = sum(final_feed)

# Output results
print(f"Final Feed: {', '.join(str(x) for x in  final_feed)}")
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")