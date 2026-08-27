"""express"""
start, end = input().split()
start = str(start.upper())
end = str(end.upper())
weight = float(input())

if start == "BKK" and end == "CNX":
    vat = 10 + (30 * weight)
    print(f"{vat:.2f}")
elif start == "CNX" and end == "UBP":
    vat = 15 + (40 * weight)
    print(f"{vat:.2f}")
elif start == "UBP" and end == "BKK":
    vat = 20 + (40 * weight)
    print(f"{vat:.2f}")
elif start == "BKK" and end == "PKT":
    vat = 25 + (50 * weight)
    print(f"{vat:.2f}")
elif start == "PKT" and end == "CNX":
    vat = 30 + (60 * weight)
    print(f"{vat:.2f}")
elif start == "UBP" and end == "PKT":
    vat = 40 + (70 * weight)
    print(f"{vat:.2f}")
else:
    print("Error")
