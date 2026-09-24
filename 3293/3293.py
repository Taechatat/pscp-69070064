'''BigFrame'''
lines = []
for _ in range(5):
    lines.append(input().rstrip())

max_len = 0
for line in lines:
    if len(line) > max_len:
        max_len = len(line)

border_len = max_len + 4
print("*" * border_len)
for line in lines:
    padding = max_len - len(line)
    print("* " + line + " " * padding + " *")
print("*" * border_len)
