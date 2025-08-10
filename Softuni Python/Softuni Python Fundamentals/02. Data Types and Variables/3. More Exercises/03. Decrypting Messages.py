
k = int(input())
n = int(input())

msg = "".join([chr(ord(input()[0])+k) for _ in range(n)])

print(msg)
    
