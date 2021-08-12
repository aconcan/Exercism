TWOS = lambda dice: dice.count(2) * 2
ONES = lambda dice: dice.count(1) * 1
THREES = lambda dice: dice.count(3) * 3
FOURS = lambda dice: dice.count(4) * 4
FIVES = lambda dice: dice.count(5) * 5
SIXES = lambda dice: dice.count(6) * 6

FULL_HOUSE = lambda dice: sum(dice) \
    if dice.count(sorted(dice)[0]) + dice.count(sorted(dice)[4]) == 5 \
        and dice.count(dice[2]) == 3 \
        else 0

FOUR_OF_A_KIND = lambda dice: sorted(dice)[2] * 4 \
    if dice.count(sorted(dice)[2]) >= 4 \
        else 0

# Direct comparison possible—function not dependent on dice values
LITTLE_STRAIGHT = lambda dice: 30 \
    if sum(dice) == 15 and len(set(dice)) == 5 \
        else 0 

BIG_STRAIGHT = lambda dice: 30 \
    if sorted(dice) == [2, 3, 4, 5, 6] \
        else 0

CHOICE = lambda dice: sum(dice)

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0

def score(dice, category):
    return category(dice)

# Alternative FULL_HOUSE using collections.Counter
# FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2,3] else 0)