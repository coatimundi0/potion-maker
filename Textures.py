from random import randrange
from random import randint
from random import choice
import pandas as pd
import os

'''
PRIMARY TEXTURE (POTION)
    It looks [TEXTURE].

    0           |   1             |   2           |   3            |   4            |
    LIQUID      |   POWDER        |   PASTE       |   GEL          |                |
    POTIONTEX   |   POTIONTASTE   |   POWDERTEX   |   POWDERSWAL   |   PASTESGELS   |
    LOOKING     |   TOUCH         |   INGESTLIQ   |   INGESTPOW    |
    CHUNKY      |   PIECES        |
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def choose_action(form): 
        # read file
    basePath = os.path.dirname(os.path.realpath(__file__))
    fileName = "AllActions.csv"
    fullPath = os.path.join(basePath, fileName)
    df = pd.read_csv(fullPath, sep=';')
        # determine what kind of item it is (liquid, powder, paste/gel)
    itemForm = form[0]
        # determine which action you take (look OR ingest/touch)
    action = randint(0, 1)

        # LIQUID (0) :::
    if itemForm == 0:
        match action:
                # LOOKING (0) :::
            case 0:
                column = 0
                # INGESTLIQ (2) :::
            case 1:
                column = 2
                # ERROR :::
            case _:
                print("choose_action ERROR1")
                return -1

        # POWDER (1) :::
    elif itemForm == 1:
        match action:
                # LOOKING (0) :::
            case 0:
                column = 0
                # INGESTPOW (3) :::
            case 1:
                column = 3
                # ERROR :::
            case _:
                print("choose_action ERROR2")
                return -1

        # PASTE (2) // GEL (3) :::
    elif (itemForm == 2) or (itemForm == 3):
        match action:
                # LOOKING (0) :::
            case 0:
                column = 0
                # TOUCH (1) :::
            case 1:
                column = 1
                # ERROR :::
            case _:
                print("choose_action ERROR3")
                return -1

        # ERROR :::
    else:
        print("choose_action ERROR4")
        return -1
    

        # determine row length
    rowLen = df[df.columns[column]].count()
        # determine the random point
    rowNum = randrange(0, (rowLen-1))
        # determine title
    phrase = df.iloc[rowNum, column]
    
    final = [phrase, action]
    return final

def pick_texture(form):
        # determine the form of the item 
    itemType = form[0]
        # read file
    basePath = os.path.dirname(os.path.realpath(__file__))
    fileName = "AllTextures.csv"
    fullPath = os.path.join(basePath, fileName)
    df = pd.read_csv(fullPath, sep=';')
        # determine which action you take (look OR ingest/touch)
    check = choose_action(form)
    action = check[1]
    phrase = ""

        # LIQUID (0) :::
    if itemType == 0:
        match action:
                # POTIONTEX (0) :::
            case 0:
                column = 0
                # POTIONTASTE (1) :::
            case 1:
                column = 1
                # ERROR :::
            case _:
                print("pick_texture ERROR1")
                return -1

        # POWDER (1) :::
    elif itemType == 1:
        match action:
                # POWDERTEX (2) :::
            case 0:
                column = 2
                # POWDERSWAL (3) :::
            case 1:
                column = 3
                # ERROR :::
            case _:
                print("pick_texture ERROR2")
                return -1

        # PASTE (2) // GEL (3) :::
    elif (itemType == 2) or (itemType == 3):
            # POWDERSWAL (4) :::
        column = 4

        # ERROR :::
    else:
        print("pick_texture ERROR3")
        return -1


        # determine row length
    rowLen = df[df.columns[column]].count()
        # determine the random point
    rowNum = randrange(0, (rowLen-1))
        # determine texture
    texture = df.iloc[rowNum, column] 
        # check chunkiness
    chunks = is_chunky()
        # full phrasing
    phrase = check[0] + " " + texture + " " + chunks

    return phrase

def is_chunky():
        # read file
    basePath = os.path.dirname(os.path.realpath(__file__))
    fileName = "AllChunks.csv"
    fullPath = os.path.join(basePath, fileName)
    df = pd.read_csv(fullPath, sep=';')
        # determine if it's chunky
    chunks = choice([True, False])
    phrase = ""

        # CHUNKS :::
    if chunks == bool(True):
        # SENTENCE START :::
            # determine row length
        rowLen = df[df.columns[0]].count()
            # determine the random point
        rowNum = randrange(0, (rowLen-1))
            # determine start
        start = df.iloc[rowNum, 0] 

        # CHUNKY PARTS :::
            # determine row length
        rowLen = df[df.columns[1]].count()
            # determine the random point
        rowNum = randrange(0, (rowLen-1))
            # determine chunky bits
        bits = df.iloc[rowNum, 1] 

        phrase = start + " " + bits

        # NOT CHUNKY :::
    elif chunks == bool(False):
        pass

        # ERROR :::
    else:
        print("is_chunky ERROR")
        return -1
    
    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # DELETE LATER: for testing purposes
from Form import make_form
form = make_form()
test = pick_texture(form)
#print(test)
