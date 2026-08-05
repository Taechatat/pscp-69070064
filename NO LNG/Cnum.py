'''สลับหมายเลข'''
num = int(input())
sym = input()
REN = int(str(num)[::-1])


if sym == "+":
    print(num, "+", REN, "=", (num + REN))
elif sym == "*":
    print(num, "*", REN, "=", (num * REN))
