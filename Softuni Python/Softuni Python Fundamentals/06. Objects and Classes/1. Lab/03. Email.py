class Email:
    def __init__(self, sender: str, receiver: str, content: str, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent
    
    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    email_info = input()
    if email_info == "Stop":
        break
    sender, receiver, content = email_info.split(maxsplit=3)
    emails += [Email(sender=sender, receiver=receiver, content=content)]

sent_email_indices = [int(x) for x in input().split(", ")]

for idx in sent_email_indices:
    emails[idx].is_sent = True

for email in emails:
    print(email.get_info())



