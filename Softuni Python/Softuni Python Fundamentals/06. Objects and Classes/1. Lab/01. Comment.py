class Comment:
    def __init__(self, username: str, content: str, likes=int(0)):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment("rmdn", "I love classes", likes=7)

print(comment.username, comment.likes, comment.content)

