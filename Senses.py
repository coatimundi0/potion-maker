from random import randrange 
from random import randint
from random import choice

'''
ADVERB + SMELLS & TASTES
    It smells [no_adverb].
    It tastes [no_adverb].

    It smells [adverb] [specific].
    It tastes [adverb] [specific].
'''

adverb = ["a lot like", "a little like", "strongly of", "pungent like", "like", "intoxicatingly like", "like spice mixed with", "like fruit mixed with", "like it's mixed with", "crisply like", "faintly like", "subtly like"]

no_adverb = ["nothing at all.", "strong... but pleasant?", "somewhat comforting... reminds you of a time where you felt safe.", "delicate. It's subtle.", "faint.", "heady.", "pungent.", "rich.", "intoxicating... how lovely...", "spicy. It's got a punch to it!", "piquant. It stings your nostrils.", "heavy.", "laden.", "fetid... like death.", "acrid and bitter.", "funky! In a bad way!", "funky! In a good way!", "unbelievably nasty.", "RANK! Yuck!", "ripe.", "sickly...", "super sour.", "kind of stale.", "super delicious. You're satisfied.", "lovely and fresh.", "crisp and sharp.", "savoury.", "tangy. Ooh!", "citrusy... you can't put your finger on it...", "coppery.", "earthy. Like soil.", "medicinal.", "smoky.", "woody."]

specific = ["an antiseptic. Very medical.", "raw fish.", "an apple.", "garlic.", "flowers.", "a hyacinth.", "jasmine flowers.", "freshly brewed tea.", "green tea.", "honeysuckle.", "nightshade..? Oh dear. Hopefully that's not bad.", "roses.", "cooked fish. Weird.", "cooked chicken.", "cooked beef.", "sweet basil.", "yummy chives.", "cilantro. (Does it taste like soap or onions to you?)", "salsa. Ooh!", "dillweed.", "fern.", "knotted marjoram.", "peppermint.", "spearmint.", "oregano!", "flat-leaf parsley.", "rosemary. Witchy.", "sage. You feel cleansed...", "tarragon.", "thyme.", "blood... oh wow.", "metal.", "steel. Maybe that's just nearby armor you're smelling...", "iron. Fae beware!", "gold. Who knew gold had a smell?", "Gaian za'atar.", "bananas!", "coconuts... tropical!", "almonds. Hope you're not allergic."]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def hasAdverb():
    descriptive = choice([True, False])
    return descriptive

def makeSmell():
    describe = hasAdverb()
    phrase = ""

    if describe == bool(True):
        verbiage = adverb[randrange(0, len(adverb)-1)]
        smell = specific[randrange(0, len(specific)-1)]
        phrase = "It smells " + verbiage + " " + smell
    elif describe == bool(False):
        smell = no_adverb[randrange(0, len(no_adverb)-1)]
        phrase = "The smell is " + smell
    else:
        print("makeSmell ERROR")
        return -1
    
    final = [phrase, smell]
    return final

def makeTaste(smell):
     # adverb?
    describe = hasAdverb()
    if describe == bool(True):
        verbiage = adverb[randrange(0, len(adverb)-1)]
        taste = specific[randrange(0, len(specific)-1)]
        phrase = "It tastes " + verbiage + " " + taste
    elif describe == bool(False):
        taste = no_adverb[randrange(0, len(no_adverb)-1)]
        phrase = "The taste is " + taste
    else:
        print("makeTaste ERROR 2")
        return -1

    # unique smell?
    det = smell[1]
    if taste == det:
        phrase = "It tastes exactly like it smells, for better or worse."
    elif taste != det:
        pass
    else: 
        print("makeTaste ERROR 1")
        return -1

    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####