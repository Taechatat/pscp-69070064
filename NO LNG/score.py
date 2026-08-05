"""score"""
def main():
    """score"""
    num = int(input())
    scorelist = []
    for _ in range(num):
        score = int(input())
        scorelist.append(score)
    scorelist.sort(reverse=True)
    while scorelist[-1] < scorelist[0]:
        scorelist.pop()
    print(scorelist[0])
    print(len(scorelist))
main()
