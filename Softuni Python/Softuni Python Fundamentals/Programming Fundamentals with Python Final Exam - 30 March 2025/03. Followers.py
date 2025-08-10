class User:
    def __init__(self, username: str):
        self.username = username
        self.likes = 0
        self.comments = 0
        self.blocked = False
    
    def __str__(self):
        return f'{self.username}: {self.likes + self.comments}'
        
    def like(self, count: int):
        self.likes += count
    
    def comment(self):
        self.comments += 1
    
    def block(self):
        self.blocked = True
        del self

class Facebook:
    __exit_command = "Log out"

    def __init__(self):
        self.users = {}
        while True:
            commands = input().split(": ")

            if commands[0] == "New follower":
                self.new_follower(commands[1])
            
            elif commands[0] == "Like":
                self.like(commands[1], int(commands[2]))
            
            elif commands[0] == "Comment":
                self.comment(commands[1])
            
            elif commands[0] == "Blocked":
                self.block(commands[1])
            
            elif commands[0] == Facebook.__exit_command:
                break
    
    def __str__(self):
        followers = []
        for user in self.users.keys():
            if not self.users[user].blocked:
                followers.append(str(self.users[user]))
        followers_listed = "\n".join(followers)
        return f'{len(followers)} followers\n{followers_listed}'

    
    def new_follower(self, username: str):
        if username not in self.users.keys():
            self.users[username] = User(username)
    
    def like(self, username: str, count: int):
        if username not in self.users.keys():
            self.users[username] = User(username) 
        self.users[username].like(count)
    
    def comment(self, username: str):
        if username not in self.users.keys():
            self.users[username] = User(username)
        self.users[username].comment()
    
    def block(self, username: str):
        if username not in self.users.keys():
            print(f"{username} doesn't exist.")
            return
        del self.users[username]
        
    
print(Facebook())
