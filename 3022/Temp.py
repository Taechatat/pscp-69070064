'''Temperature'''
temp = float(input())
BEF = input()
AFT = input()

if BEF != "C":
    if BEF == "k":
        temp =  temp - 273.15
    elif BEF == "F":
        temp = (temp - 32)*5/9
    elif BEF == "R":
        temp = (temp*5/9)-273.15

if AFT == "C":
    print(f"{temp:.2f}")
elif AFT == "K":
    print(f"{temp + 273.15:.2f}")
elif AFT == "F":
    print(f"{temp*9/5+32:.2f}")
elif AFT == "R":
    print(f"{(temp+273.15)*9/5:.2f}")
