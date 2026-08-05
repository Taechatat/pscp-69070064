'''DISTANCE'''
import math as m
a, b, c = map(int, input().split())
e, f, g = map(int, input().split())

d = m.sqrt(((a-e)**2)+((b-f)**2)+((c-g)**2))
print(f"{d:.2f}")
