contest = {}

submissions = {}

banned_users = []

while True:
    submission_info = input()

    if submission_info == "exam finished":
        print("Results:")
        for username in contest:
            if username not in banned_users:
                print(f"{username} | {contest[username]}")
        
        print("Submissions:")
        for language in submissions:
            print(f"{language} - {len(submissions[language])}")
        break

    if "-banned" in submission_info:
        username = submission_info.split('-')[0]
        banned_users.append(username)
        continue

    username, language, points = submission_info.split('-')
    points = int(points)

    if language not in submissions:
        submissions[language] = []
    
    submissions[language].append({
        "username": username,
        "points": points        
    })

    if username not in contest:
        contest[username] = points
    
    contest[username] = max(contest[username], points)
