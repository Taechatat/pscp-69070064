'''RGB Mixed'''
R1,G1,B1 = map(int, input().split())
R2,G2,B2 = map(int, input().split())

Rr = (R1 + R2) // 2
Gr = (G1 + G2) // 2
Br = (B1 + B2) // 2

print(Rr, Gr, Br)
