'''GAME ARAI MAIRU'''
n = int(input())
score = 0

for _ in range(n):
    cmd = input()
    if cmd == "+":
        score += 10
    elif cmd == "-":
        score -= 5

print(score)
