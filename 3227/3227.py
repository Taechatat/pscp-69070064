'''ไพ่ 44 ใบ'''
card = input().upper()
rank = card[:-1]
suit = card[-1]
RANK_FULL = ""
SUIT_FULL = ""

if rank == "A":
    RANK_FULL = "ace"
elif rank == "J":
    RANK_FULL = "jack"
elif rank == "Q":
    RANK_FULL = "queen"
elif rank == "K":
    RANK_FULL = "king"
else:
    RANK_FULL = rank

if suit == "D":
    SUIT_FULL = "diamonds"
elif suit == "H":
    SUIT_FULL = "hearts"
elif suit == "S":
    SUIT_FULL = "spades"
elif suit == "C":
    SUIT_FULL = "clubs"

print(RANK_FULL, "of", SUIT_FULL)
