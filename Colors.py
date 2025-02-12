from random import sample, randrange, randint, choice
import pandas as pd
import os

'''
Colors
    The mixture inside the container is [COLORSHIFT/RAINBOW/CLEAR/COLOR].
    The item inside the container is [COLOR1] with little flecks of [COLOR2]

    0            |   1         |   2       |   3            |
    COLORSHIFT   |   RAINBOW   |   CLEAR   |   COLORS       |
'''

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # read file
basePath = os.path.dirname(os.path.realpath(__file__))
fileName = "AllColors.csv"
fullPath = os.path.join(basePath, fileName)
df = pd.read_csv(fullPath, sep=';')

def make_color():
    numColors = choice([True, False])
    start = ""

        # ONE (true) :::
    if numColors == bool(True):
        column = randint(0, 3)
            # determine row length
        rowLen = df[df.columns[column]].count()
            # determine the random point
        rowNum = randrange(0, (rowLen-1))
            # determine color
        start = "The mixture inside the container is"
        color = df.iloc[rowNum, column]

            # SHIFT (0) // RAINBOW (1) // CLEAR (2) :::
        if (column == 0) or (column == 1) or (column == 2):
            phrasing = start + " " + color
            # COLOR (3) :::
        elif column == 3:
            phrasing = start + " " + color + "."
            # ERROR :::
        else:
            print("make_color ERROR1")
            return -1

        # TWO (false) :::
    elif numColors ==  bool(False):
            # determine row length
        rowLen = df[df.columns[3]].count()
            # determine first random color
        colorNums = sample(range(0, (rowLen-1)), 2)
        colorOne = df.iloc[colorNums[0], 3]
        colorTwo = df.iloc[colorNums[1], 3]

        start = "The item inside the container is"
        mid = "with little flecks of"
        phrasing = start + " " + colorOne + " " + mid + " " + colorTwo + "."

        # ERROR :::
    else:
        print("make_color ERROR2")
        return -1
    
    return phrasing

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

    # DELETE LATER: for testing purposes
test = make_color()
#print(test)
