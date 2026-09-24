'''หาจำนวนเฉพาะ'''
n = input().split()
start = int(n[0])
end = int(n[1])
prime = []
for i in range(start, end+1):
    if i <= 1:
        continue
    isprime = True
    for p in range(2,i):
        if not i % p:
            isprime = False
            break
    if isprime:
        prime.append(i)
if prime:
    print(*prime)
print("Total primes:" , len(prime))
