'''Calculator'''
n = int(input())
L = len(str(n))
ONE = int('1' * L)

if n == 1:
    print("1")
else:
    print((L+1)*n - ONE + L)
