sumscore = float(input())
maxscore = float(input())

remaining_score = sumscore - maxscore

min_score = remaining_score - maxscore


if min_score < 0:
    min_score = 0


if (maxscore - min_score > 2) and (sumscore >= maxscore) and (sumscore <= 3 * maxscore):
    print("Surprising")
else:
    print("Not surprising")
