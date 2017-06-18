'''
csvRead - dealing with NaN

'''

import math
import numpy as np

def str2num(string):
    try:
        num = float(string)
    except ValueError:
        return float('nan')
    return num

def csvRead(fileName):
    file = open(fileName)
    data = file.readlines()
    row = len(data)
    col = len(data[0].strip().split(','))
    arr = np.zeros((row,col))
    for i in range(row):
        line = data[i].strip().split(',')
        for j in range(col):
            arr[i][j] = str2num(line[j])
    file.close()
    return arr

def csvReadNum(fileName):
    file = open(fileName)
    data = file.readlines()
    row = len(data)
    col = len(data[0].strip().split(','))
    arr = np.zeros((row,col))
    for i in range(row):
        line = data[i].strip().split(',')
        for j in range(col):
            arr[i][j] = str2num(line[j])
    file.close()
    # detect the rows with all 'NaN' entries
    deleteRows = []
    for i in range(row):
        cnt = 0
        for j in range(col):
            if(math.isnan(arr[i][j])):
                cnt = cnt + 1
        if(cnt==col):
            deleteRows.append(i)
            
    # detect the cols with all 'NaN' entries
    deleteCols = []
    for j in range(col):
        cnt = 0
        for i in range(row):
            if(math.isnan(arr[i][j])):
                cnt = cnt + 1
        if(cnt==row):
            deleteCols.append(j)

    # delete rows/cols
    #print(deleteRows)
    #print(deleteCols)
    arr = np.delete(arr, deleteRows, 0)
    arr = np.delete(arr, deleteCols, 1)
    return arr

# main()
train = csvRead('trainLabels.csv')
print(train.shape)

train1 = csvReadNum('trainLabels.csv')
print(train1.shape)

