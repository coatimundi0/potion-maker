from random import randrange
from random import randint

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

'''
TIME PERIOD
    The effect of the item lasts [NUMBER] [TIME].
'''
time_period = ["rounds", "hours", "days"]
dice = ["d4", "d6", "d8", "d10", "d12", "d20"]

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

def makeTimePeriod():
    all_day = randint(0, 10)
    phrase = ""

    if 0 <= all_day <= 5:
        phrase = "The effect of the item lasts for 24-hours."
    elif 6 <= all_day <= 7:
        num_rolls = randrange(1, 5)
        dice_rolled = dice[randrange(0, len(dice)-1)]
        period = time_period[randrange(0, len(time_period)-1)]

        phrase = "The effect of the item lasts " + f"{num_rolls}" + dice_rolled + " " + period  + "."
    elif 8 <= all_day <= 9:
        time = randrange(1, 10)
        period = time_period[randrange(0, len(time_period)-1)]

        phrase = "The effect of the item lasts " + f"{time}" + " " + period  + "."
    else: 
        print("makeTimePeriod ERROR")
        return -1
    
    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####