'''SurprisingVote'''
sumscore = float(input())
maxscore = float(input())

if maxscore-(sumscore-(maxscore*2)) < 2:
    print("Not surprising")
else :
    print("Surprising")
