from random import randrange 
from random import randint

'''
FULL TITLE
    The label reads [TITLE] of [EFFECT].
    The label reads [EFFECT] [TITLE].
'''

phrasing = ["The label says it's called ", "The label reads ",
            "It says ", "It's called ", "Apparently it's called ", 
            "The name of it is ", "The name is ", "The name says "]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeFullTitle(title, effect):    
    verbiage = randint(0, 1)
    says = phrasing[randrange(0, len(phrasing)-1)]
    phrase = ""

    if verbiage == 0:
        phrase = says + title + " of " + effect[0] + "."
    elif verbiage == 1: 
        phrase = says + effect[0] + " " + title + "."
    else: 
        print("There has been an error.")
        return -1
    
    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 