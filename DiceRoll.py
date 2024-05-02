from random import randrange

dice = ["d4", "d6", "d8", "d10", "d12", "d20"]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def effectLength():
    num_rolls = randrange(1, 5)
    dice_rolled = dice[randrange(0, len(dice)-1)]

    phrase = f"(The dice roll is {num_rolls}" + dice_rolled + "."

    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####