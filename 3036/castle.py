'''castle'''
import math
n = int(input())

if n == 1:
    print("0")
else:
    row = math.ceil(math.sqrt(n))
    col = n - (row - 1) ** 2
    if not col % 2 :
        print((2 * row) - 3)
    else:
        print((2 * row) - 2)
