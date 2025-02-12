from random import randrange
from random import randint
import pandas as pd
import os

'''
TITLE
    The label reads [TITLE] of [EFFECT].
    The label reads [EFFECT] [TITLE].

    0        |   1        |   2       |   3
    LIQUID   |   POWDER   |   PASTE   |   GEL
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

basePath = os.path.dirname(os.path.realpath(__file__))
fileName = "AllTitles.csv"
fullPath = os.path.join(basePath, fileName)
df = pd.read_csv(fullPath, sep=';')

def make_title(form):
        # determine the form of the item 
    titleForm = form[0]
        # determine row length
    rowLen = df[df.columns[titleForm]].count()
        # determine the random point
    rowNum = randrange(0, (rowLen-1))
        # determine title
    title = df.iloc[rowNum, titleForm]


        # PHRASING
    phrase = ["Effect ", " of Effect"]
    detPhrase = randint(0, 1)
    phrasing = ""

    match detPhrase:
            # Effect [Title] (0) :::
        case 0:
            phrasing = phrase[detPhrase] + title

            # [Title] of Effect (1) :::
        case 1:
            phrasing = title + phrase[detPhrase]

            # ERROR :::
        case _:
                print("make_title ERROR")
                return -1

    return phrasing 

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # DELETE LATER: for testing purposes
from Form import make_form
form = make_form()
test = make_title(form)
#print(test)
