from random import randrange
from random import randint
from random import choice
import pandas as pd
import os

'''
ADVERB + SMELLS & TASTES
    It smells [no_adverb].
    It tastes [no_adverb].

    It smells [adverb] [specific].
    It tastes [adverb] [specific].

    0         |   1       |   2     
    ADVERBS   |   SENSE   |   NOADVERB
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

basePath = os.path.dirname(os.path.realpath(__file__))
fileName = "AllSenses.csv"
fullPath = os.path.join(basePath, fileName)
df = pd.read_csv(fullPath, sep=';')

def pick_sense(describe):
    sense = randint(0, 1)
    verb = ""

        # ADVERB (true) :::
    if describe == bool(True):
        match sense:
                # TASTE (0) :::
            case 0:
                verb = "tastes"
                # SMELL (1) :::
            case 1:
                verb = "smells"
                # ERROR :::
            case _:
                print("pick_sense ERROR1")
                return -1

        #  NOADVERB (false)
    elif describe == bool(False):
        match sense:
                # TASTE (0) :::
            case 0:
                verb = "taste"
                # SMELL (1) :::
            case 1:
                verb = "smell"
                # ERROR :::
            case _:
                print("pick_sense ERROR2")
                return -1

        # ERROR :::
    else:
        print("pick_sense ERROR3")
        return -1
    
    return verb
    

def make_sense():
        # DESCRIPTORS
    describe = choice([True, False])
    phrase = ""
    desc = ""

        # ADVERB (true) :::
    if describe == bool(True):
                # ADVERB (0) :::
            # determine row length
        rowLen = df[df.columns[0]].count()
                # determine the random point
        rowNum = randrange(0, (rowLen-1))
                # determine adverb
        adverb = df.iloc[rowNum, 0]

                # SCENT (1) :::
            # determine row length
        rowLen = df[df.columns[1]].count()
            # determine the random point
        rowNum = randrange(0, (rowLen-1))
           # determine sense
        desc = df.iloc[rowNum, 1]
            # determine verb
        verb = pick_sense(describe)

        phrase = "It " + verb + " " + adverb + " " + desc

        # NOADVERB (false) :::
    elif describe == bool(False):
            # determine row length
        rowLen = df[df.columns[2]].count()
                # determine the random point
        rowNum = randrange(0, (rowLen-1))
                # determine scent
        desc = df.iloc[rowNum, 2]
            # determine verb
        verb = pick_sense(describe)
        phrase = "The " + verb + " is " + desc

        # ERROR :::
    else:
        print("make_sense ERROR2")
        return -1
    
    final = [phrase, desc]
    return final

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # DELETE LATER: for testing purposes
test = make_sense()
print(test[0])
