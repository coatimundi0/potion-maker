from random import randrange
from random import randint

        # contains: serving_size, dice_rolls, pick_accuracy

'''
SERVING SIZE
    Looks like there's [SIZE] in here.

    0-69   |   70-84   |   85-94    |   95-99
    ONCE   |   TWICE   |   THRICE   |   PARTY
    (70)   |   (15)    |   (10)     |   (5)
'''

def serving_sizes():
        # determine the serving sizes
    servings = randint(0, 99)

        # ONCE (70) :::
    if 0 <= servings <= 69:
        size = "just a single serving"
        # TWICE (15) :::
    elif 70 <= servings <= 84:
        size = "two servings"
        # THRICE (10) :::
    elif 84 <= servings <= 94:
        size = "three servings"
        # PARTY (5) :::
    elif 95 <= servings <= 99:
        size = "enough for everyone in the party to have some"
    else: 
        print("serving_sizes ERROR")
        return -1

        # put it all together
    phrase = f"(Looks like there's {size} in here.)"
    return phrase

    # DELETE LATER: for testing purposes
test = serving_sizes()
#print(test)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

'''
DICE ROLL
    The dice roll is [NUM_ROLLS][DICE].

    0-4  |   5-9  | 10-44  | 45-59  | 60-74  |  75-84  |  85-94  |  95-99
    d2   |   d3   |   d4   |   d6   |   d8   |   d10   |   d12   |   d20

    later i will probably implement an option to choose the dice you want to be included,
    in case no one has a d2/d3 or doesnt want d20s rolled...
    no d100s either

'''

def dice_rolls():
        # determine the dice
    pickDice = randint(0, 99)
    dice = ""

            # PICK DICE :::
        # d2 (5) :::
    if   0 <= pickDice <= 4:
        dice = "d2"
        # d3 (5) :::
    elif 5 <= pickDice <= 9:
        dice = "d3"
        # d4 (35) :::
    elif 10 <= pickDice <= 44:
        dice = "d4"
        # d6 (15) :::
    elif 45 <= pickDice <= 59:
        dice = "d6"
        # d8 (15) :::
    elif 60 <= pickDice <= 74:
        dice = "d8"
        # d10 (10) :::
    elif 75 <= pickDice <= 84:
        dice = "d10"
        # d12 (10) :::
    elif 85 <= pickDice <= 94:
        dice = "d12"
        # d20 (5) :::
    elif 95 <= pickDice <= 99:
        dice = "d20"
        # ERROR :::
    else:
        print("dice_rolls ERROR")
        return -1
    
        # right now there's a 25% chance of any of them. maybe edit that later
    num_rolls = randrange(1, 4)
        # put it all together
    phrase = f"(The dice roll is {num_rolls}{dice}.)"
    return phrase

    # DELETE LATER: for testing purposes
test = dice_rolls()
#print(test)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

'''
ACCURACY [ONLY IF GIVEN TITLE]
    there is a 90% chance that it does exactly what is listed.
    if it's not accurate, player must beat the random number.
'''

def pick_accuracy():
        # determine if the listed effect is accurate
    accuracy = randint(0, 99)
    phrase = ""

        # ACCURATE (0 - 89) :::
    if 0 <= accuracy <= 89:
        phrase = "Oh boy! The item's effect is exactly as listed."
        deter = bool(True)

        # INACCURATE (90 - 99) :::
    elif 90 <= accuracy <= 99:
            # determine the number to beat
        acc = randint(0, 99)
        phrase = f"There's some fine print on this item that says it has {acc}% accuracy...\n(Roll 1d100; the result must be equal to or higher than {acc} to have the listed effect.)"
        deter =  bool(False)

        # ERROR :::
    else: 
        print("pick_accuracy ERROR")
        return -1

    final = [phrase, deter]
    return phrase

    # DELETE LATER: for testing purposes
test = pick_accuracy()
#print(test)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 


