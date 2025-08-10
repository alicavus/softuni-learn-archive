contests = {}
user_submissions = {}

while True:
    input_line = input()

    if input_line == "no more time":
        for contest in contests.keys():
            curr_contest = dict(sorted(contests[contest].items(), key = lambda item: [-item[1], item[0]]))
            print(f"{contest}: {len(contests[contest].keys())} participants")
            for idx, curr_user in enumerate(curr_contest.items(), 1):
                print(f"{idx}. {curr_user[0]} <::> {curr_user[1]}")

        #print(user_submissions.items())
        user_submissions = {user:sum(points.values()) for user, points in user_submissions.items()}
        user_submissions = dict(sorted(user_submissions.items(), key = lambda item: [-item[1], item[0]]))
        print("Individual standings:")
        for idx, curr_user in enumerate(user_submissions.items(), 1):
            print(f"{idx}. {curr_user[0]} -> {curr_user[1]}")

        break

    username, contest, points = input_line.split(" -> ")

    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = int(points)
    else:
        contests[contest][username] = max(contests[contest][username], int(points))
    
    
    if username not in user_submissions:
        user_submissions[username] = {}
    if contest not in user_submissions[username]:
        user_submissions[username][contest] = int(points)
    else:
        user_submissions[username][contest] = max(user_submissions[username][contest], int(points))
    

