'''Season'''
mot = int(input())
day = int(input())

if day >= 21:
    if not mot % 3:
        mot += 1
        if mot > 12:
            mot -= 12

if mot in {1, 2, 3}:
    print("winter")
elif mot in {4, 5, 6}:
    print("spring")
elif mot in {7, 8, 9}:
    print("summer")
elif mot in {10, 11, 12}:
    print("fall")
