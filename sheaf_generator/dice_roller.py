import random


# Basic Die Roller, Defaults to 1D6
def basic_roll(dice_pool=1, sides=6):
    # Weirdly, randrange seems to be way faster than randint
    return [random.randrange(sides) + 1 for _ in range(0, dice_pool)]


# Exploding 6's Roller, Shadowrun 3rd Editions most common roll.
# Any dice that rolls a 6 is rolled until it is no longer 6 and the total of all rolls for that die are added together.
def sr3_roll(dice_pool=1, sides=6):
    rolls = basic_roll(dice_pool, sides)
    sixes = [x for x in rolls if x == 6]
    rolls = [x for x in rolls if x < 6]
    if sixes:
        sixes = [x + y for x, y in zip(sixes, sr3_roll(len(sixes), 6))]
        rolls.extend(sixes)
    return rolls


# Perform a success test by comparing a list of rolls against a Target Number
def success_test(rolls, threshold=4):
    count = 0
    for roll in rolls:
        if roll >= threshold:
            count += 1
    return count
