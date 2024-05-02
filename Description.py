from random import randrange 
from random import randint

'''
SUBLABEL 
    YES --> The label also [HAS_DESCRIPTION].
    NO  --> (IGNORE)
'''
explanation = "describes the effects. How convenient for you!"
description = ["has a full decription in ornate Elvish...",
               "has a short decription in illegible Dwarven runes. Weird!",
               "has a description of the side effects... in Gnomish.",
               "says \"USE ONLY IN EMERGENCIES\". Is this an emergency?",
               "says \"Whatever happens isn't my fault.\"",
               "says \"Not Tested On Animals!\"",
               "says \"New, Delicious Flavor!\"",
               "has a full recipe for it. Lucky, if we want to make it ourselves...",
               "has a decription is in Gaian Elvish. Inconvenient.",
               "has a description is in Draconic."
            ]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeDescription():
    ### ONLY IF IT HAS A LABEL
    has_decription = description[randrange(0, len(description)-1)]
    phrase = ""
    effect_description = bool(False)

    sublabel = randint(0,2)
    if sublabel == 0:
        phrase = "Looks like there's nothing else on it."
    elif sublabel == 1:
        phrase = "The label also " + explanation
        effect_description = bool(True)
    elif sublabel == 2:
        phrase = "The label also " + has_decription
    else: 
        print("makeDescription ERROR")
        return -1
    
    final = [phrase, effect_description]
    return final

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 