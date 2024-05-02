from random import randrange 
from random import randint
from random import choice

'''
ACCURACY (If Given Title)
    YES --> Accurate
    NO  --> Opposite
'''
accurate = ["Seems legit.", "This feels extra magical.", "This feels weird...", "You suppose you can trust it."]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def pickAccuracy():
    # accuracy ::  ACCURATE (0-89); OPPOSITE (90-100)
    accuracy = randint(0, 99)

    if 0 <= accuracy <= 89:
        phrase = accurate[randrange(0, len(accurate)-1)]
        deter = bool(True)
    elif 90 <= accuracy <= 99:
        acc = randint(0, 99)
        phrase = f"There is a {acc}% chance that the item will have the opposite effect. Roll 1d100 and get higher than {acc}."
        deter =  bool(False)
    else: 
        print("pickAccuracy ERROR")
        return -1

    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####