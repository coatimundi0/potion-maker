from random import randrange 
from random import randint
import numpy as np

'''
EFFECT
    The label reads [TITLE] of [ARRAY[X,0]].
    The label reads [EFFECT] [TITLE].

EFFECT DESCRIPTION
    This item [ARRAY[X,1]]

    # STOPPED AT :: 11. STONESKIN
'''
instant = np.array([
    ["POSITIVE", "NEGATIVE"],
    ["Healing", "instantly regenerates health."], ["Poison", "instantly damages health."],
    ["Vigor", "instantly provides 1d12 temporary health points."], ["Lethargy", "instantly provides 1d12 temporary negative health points."]
    ])
timed = np.array([
    ["POSITIVE", "NEGATIVE"],
    ["Vitality", "slowly regenerates health."], ["Lethargy", "slowly damages health."],
    ["Might", "provides some attack roll bonus."], ["Dizziness", "delivers some attack roll penalty."],
    ["Courage", "gives immunity to fear."], ["Cowardice", "instantly make a Will save and risk being frightened."],
    ["Giant Strength", "changes the target's STR to 25 (+7)."], ["Tiny Strength", "changes the target's STR to 3 (-4)"],
    ["Flame Resistance", "grants some resistance to fire damage."], ["Flame Weakness", "deals some weakness to fire damage."],
    ["Cold Resistance", "grants some resistance to cold damage."], ["Cold Weakness", "deals some weakness to cold damage."],
    ["Acid Resistance", "grants some resistance to acid damage."], ["Acid Weakness", "deals some weakness to acid damage."],
    ["Shock Resistance", "grants some resistance to electric damage."], ["Electro Weakness", "deals some weakness to electric damage."],
    ["Poison Resistance", "grants some resistance on saves against poisoning."], ["Poison Weakness", "poisons deal double damage."],
    ["Extra Positivity", "doubles effects of positive energy."], ["Inverse Positivity", "reverses the effects of positive energy."]
    ])
permanent = np.array([
    ["POSITIVE", "NEGATIVE"],
    ["Healing", "permanently regenerates health."], ["Poison", "permanently damages health."]
    ])

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

def determineLength():
    # length ::  INSTANT (0-29); TIMES (30-89); PERMANENT (90-100)
    length = randint(0, 100)

    if 0 <= length <= 29:
        #effect = makeEffect(accuracy, instant)
        effect_number = randrange(1, len(instant)-1)
        effect = instant[effect_number]
    elif 30 <= length <= 89:
        #effect = makeEffect(accuracy, timed)
        effect_number = randrange(1, len(timed)-1)
        effect = timed[effect_number]
    elif 90 <= length <= 100:
        #effect = makeEffect(accuracy, permanent)
        effect_number = randrange(1, len(permanent)-1)
        effect = permanent[effect_number]
    else: 
        print("determineLength ERROR")
        return -1
    
    return effect

'''
def makeEffect(accuracy, array):
    effect_number = randrange(1, len(array)-1)


    # ODD --> POSITIVE
    if effect_number % 2 != 0:
        if accuracy[0] == bool(False):
            # OPPOSITE --> NEGATIVE
            effect = array[effect_number+1]
            
            true_name = array[effect_number, 0]
            true_desc = array[effect_number, 1]
            phrase = "TRUE EFFECT: [" + true_name + ", " + true_desc
            #print(phrase)
        elif accuracy[0] == bool(True): 
            # ACCURATE --> POSITIVE
            effect = array[effect_number]
        else: 
            print("makeEffect ERROR ODD")
            return -1
        
    # EVEN --> NEGATIVE
    elif effect_number % 2 == 0:
        if accuracy[0] == bool(False):
            # OPPOSITE --> POSITIVE
            effect = array[effect_number-1]
            #print(phrase)
        elif accuracy[0] == bool(True): 
            # ACCURATE --> NEGATIVE
            effect = array[effect_number]
        else: 
            print("makeEffect ERROR EVEN")
            return -1
    
    else:
        print("makeEffect ERROR")
        return -1

    return effect

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
'''