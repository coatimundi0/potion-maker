import pandas as pd
import os

'''
    test page. it reads the file and prints the columns, one by one
    just to ensure that the whole reading process works!
'''

fileName = "AllColors.csv"

def read_each_column():
        # open file
    basePath = os.path.dirname(os.path.realpath(__file__))
    fullPath = os.path.join(basePath, fileName)
    df = pd.read_csv(fullPath, sep=';')

        # get the number of columns
    colNum = len(df.columns)
        # declare iterator
    num = 0

        # iterate through each column. print it! 
    for num in range(0, colNum):
        columnName = df.columns[num]
        print('')
        print(columnName)

            # row, ignoring any NaN entries
        rowLen = df[df.columns[num]].count()
        #print(rowLen)

            # ignoring the header row, so start at 1
        number = 0
        for number in range(0, rowLen):
            columnEntry = df.loc[number, columnName]
            print(number, ": ", columnEntry)

read_each_column()
