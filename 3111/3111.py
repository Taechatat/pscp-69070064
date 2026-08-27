"""sahaprachachatt"""
member = input()
n = int(input())
total = 0
for _ in range(n):
    price = float(input())
    total += price
if member == 'Y':
    final_price = total * 0.95
elif member == 'N' and total >= 500:
    final_price = total * 0.97
else:
    final_price = total
final_price += 0.000000001
print(f"{final_price:.2f}")
