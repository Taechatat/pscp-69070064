"""Arcade of Time: Store Check"""
num,_ = map(int,input().split())
openstore = [0] * 1441
for _ in range(num):
    start, stop = map(int, input().split())
    for minute in range(start, stop):
        openstore[minute] += 1
check_times = list(map(int, input().split()))
results = []
for k in check_times:
    results.append(openstore[k])
print(*results)
