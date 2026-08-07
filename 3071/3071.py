'''HARNNNN'''
A = int(input())
B = int(input())
d = int(input())
r = int(input())
F = 0

for i in range(A, B+1,):
    if  i % d == r:
        F += 1
print(F)
