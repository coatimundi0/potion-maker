from random import randrange
from random import randint
import pandas as pd
import os

'''
CONTAINER
    The item you pick up is [CONTAINER].

    0        |   1        |   2       |   3         |   4
    LIQUID   |   POWDER   |   PASTE   |   GEL       |   
    INGEST   |   SPLASH   |   DROPS   |   POWDER    |   OTHER
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

basePath = os.path.dirname(os.path.realpath(__file__))
fileName = "AllContainers.csv"
fullPath = os.path.join(basePath, fileName)
df = pd.read_csv(fullPath, sep=';')

def make_container(form):
        # determine the form of the item 
    itemType = form[0]
        # declare column number determinant
    colNum = 0

        # LIQUID (0) :::
    if itemType == 0:
            # INGESTIBLE (0) :::
        if form[2] == bool(True):
            colNum = 0
            # SPLASH (1) // DROPLET (2) :::
        else: 
            colNum = randint(1, 2)

        # POWDER (1) :::
    elif itemType == 1:
            # POWDER (3)
        colNum = 3
        
        # PASTE (2) / GEL (3) :::
    elif (itemType == 2) or (itemType == 3):
            # OTHER (4)
        colNum = 4

        # ERROR :::
    else:
        print("make_container ERROR")
        return -1
    

        # determine row length
    rowLen = df[df.columns[colNum]].count()
        # determine the random point
    rowNum = randrange(0, (rowLen-1))
        # determine the container
    container = df.iloc[rowNum, colNum]
    
        # PHRASING
    phrasing = "The item you pick up is "
    phrase = phrasing + container + "."
    final = [phrase, colNum]
    return final

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
    # DELETE LATER: for testing purposes
from Form import make_form
form = make_form()
test = make_container(form)
#print(test[0])
