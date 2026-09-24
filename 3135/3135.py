'''ของขวัญและขโมย'''
n, k, t = map(int, input().split())
visited = set()
current_person = 1
count = 0
while True:
    if current_person in visited:
        break
    visited.add(current_person)
    count += 1
    if current_person == t:
        break
    current_person = (current_person + k - 1) % n + 1

print(count)
