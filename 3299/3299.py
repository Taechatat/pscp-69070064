'''FLOWERRRR'''
L, N = map(int, input().split())
band = 1
total_slots = 0

while True:
    if band == 1:
        capacity = (L * (L + 1)) // 2
    else:
        capacity = (L * (L + 1)) // 2 + (band - 1) * (L * L)

    total_slots += capacity

    if N <= total_slots:
        print(band)
        break

    band += 1
