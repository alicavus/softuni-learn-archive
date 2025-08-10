
def best_user(submissions: dict) -> dict:
    '''
    Returns the best user and his points    
    '''
    best_user = None
    best_points = 0

    for user in submissions.keys():
        curr_user = user
        curr_points = sum(submissions[user].values())

        if curr_points > best_points:
            best_points = curr_points
            best_user = curr_user
    return {"user": best_user, "points": best_points}

def print_results(submissions: dict) -> None:
    print("Ranking:")
    for user in sorted(submissions.keys()):
        print(user)
        for contest, result in sorted(submissions[user].items(), key=lambda item: -item[1]):
            print(f"#  {contest} -> {result}")

contests = {}

submissions = {}

while True:
    input_line = input()

    if input_line == "end of contests":
        break

    contest, password = input_line.split(":", 1)

    contests[contest] = password

while True:
    input_line = input()

    if input_line == "end of submissions":
        break

    contest, password, username, points = input_line.split("=>")

    if contest not in contests.keys() or contests[contest] != password:
        continue

    if username not in submissions:
        submissions[username] = {}
    if contest not in submissions[username]:
        submissions[username][contest] = int(points)
    else:
        submissions[username][contest] = max(submissions[username][contest], int(points))


best_user = best_user(submissions)

print(f'Best candidate is {best_user["user"]} with total {best_user["points"]} points.')

print_results(submissions)

            




